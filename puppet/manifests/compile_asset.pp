## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/', '/bin/']}

## variables
$compilers       = ['uglifyjs', 'sass', 'imagemin']
$directory_src   = ['js', 'scss', 'img']
$directory_asset = ['js', 'css', 'img']

## dynamically create compilers
$compilers.each |Integer $index, String $compiler| {
    ## create asset directories
    file {"/vagrant/web_interface/static/${directory_asset[$index]}/":
        ensure => 'directory',
        before => File["${compiler}-startup-script"],
    }

    ## create startup script (heredoc syntax)
    #
    #  @("EOT"), the use double quotes on the end tag, allows variable interpolation within the puppet heredoc.
    file {"${compiler}-startup-script":
        path    => "/etc/init/${compiler}.conf",
        ensure  => 'present',
        content => @("EOT"/$),
                   #!upstart
                   description 'start ${compiler}'

                   ## start job defined in this file after system services, and processes have already loaded
                   #       (to prevent conflict).
                   #
                   #  @vagrant-mounted, an event that executes after the shared folder is mounted
                   #  @[2345], represents all configuration states with general linux, and networking access
                   start on (vagrant-mounted and runlevel [2345])

                   ## stop upstart job
                   stop on runlevel [!2345]

                   ## restart upstart job continuously
                   respawn

                   # required for permission to write to '/vagrant/' files (pre-stop stanza)
                   setuid vagrant
                   setgid vagrant

                   ## run upstart job as a background process
                   expect fork

                   ## start upstart job
                   #
                   #  @chdir, change the current working directory
                   chdir /vagrant/puppet/scripts/
                   exec ./${compiler}

                   ## log start-up date
                   #
                   #  @[`date`], current date script executed
                   pre-start script
                       echo "[`date`] ${compiler} service watcher starting" >> /vagrant/log/${compiler}.log 
                   end script

                   ## log shut-down date, remove process id from log before '/vagrant' is unmounted
                   #
                   #  @[`date`], current date script executed
                   pre-stop script
                       echo "[`date`] ${compiler} watcher stopping" >> /vagrant/log/${compiler}.log
                   end script
                   | EOT
               notify  => Service["${compiler}"],
        }

    ## start ${compiler} service
    service {"${compiler}":
        ensure => 'running',
        enable => 'true',
        notify  => Exec["touch-${directory_src[$index]}"],
    }

    ## touch source: ensure initial build compiles every source files
    #
    #  Note: inotifywait watches close_write, move, and create. However, the source files will already exist before
    #        this 'inotifywait', since the '/vagrant' directory will already have been mounted on the initial build.
    exec {"touch-${directory_src[$index]}":
        command => "touch /vagrant/src/${directory_src[$index]}/*",
        refreshonly => true,
    }
}