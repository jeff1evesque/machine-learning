## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/', '/sbin/', '/bin/', '/usr/share/']}

## variables: the order of the following array variables are important
$compilers       = ['uglifyjs', 'sass', 'imagemin']
$directory_src   = ['js', 'scss', 'img']
$directory_asset = ['js', 'css', 'img']

## dynamically create compilers
$compilers.each |Integer $index, String $compiler| {
  ## create asset directories
  file {"/vagrant/interface/static/${directory_asset[$index]}/":
    ensure => 'directory',
    before => File["${compiler}-startup-script"],
  }

  ## create startup script: for webcompilers, using heredoc syntax
  #
  #  @("EOT"), the use double quotes on the end tag, allows variable
  #      interpolation within the puppet heredoc.
  file {"${compiler}-startup-script":
    path    => "/etc/init/${compiler}.conf",
    ensure  => 'present',
    content => @("EOT"),
      #!upstart
      description 'start ${compiler}'

      ## start job defined in this file after system services, and processes
      #      have already loaded (to prevent conflict).
      #
      #  @vagrant-mounted, an event that executes after '/vagrant' is mounted
      #  @[2345], represents all configuration states with general linux, and
      #      networking access.
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

      ## log shut-down date, then remove process id from log before '/vagrant'
      #      is unmounted.
      #
      #  @[`date`], current date script executed
      pre-stop script
        echo "[`date`] ${compiler} watcher stopping" >> /vagrant/log/${compiler}.log
      end script
    | EOT
    notify  => Exec["dos2unix-upstart-${compiler}"],
  }

  ## convert clrf (windows to linux) in case host machine is windows.
  #
  #  @notify, ensure the webserver service is started. This is similar to an
  #      exec statement, where the 'refreshonly => true' would be implemented
  #      on the corresponding listening end point. But, the 'service' end point
  #      does not require the 'refreshonly' attribute.
  exec {"dos2unix-upstart-${compiler}":
    command => "dos2unix /etc/init/${compiler}.conf",
    refreshonly => true,
    notify  => Exec["dos2unix-bash-${compiler}"],
  }

  ## convert clrf (windows to linux) in case host machine is windows.
  #
  #  @notify, ensure the webserver service is started. This is similar to an
  #      exec statement, where the 'refreshonly => true' would be implemented
  #      on the corresponding listening end point. But, the 'service' end point
  #      does not require the 'refreshonly' attribute.
  exec {"dos2unix-bash-${compiler}":
    command => "dos2unix /vagrant/puppet/scripts/${compiler}",
    refreshonly => true,
    notify  => Service["${compiler}"],
  }

  ## start ${compiler} service
  service {"${compiler}":
    ensure => 'running',
    enable => 'true',
    notify  => Exec["touch-${directory_src[$index]}-files"],
  }

  ## touch source: ensure initial build compiles every source file.
  #
  #  @touch, changes the modification time to the current system time.
  #
  #  Note: the current inotifywait implementation watches close_write, move,
  #        and create. However, the source files will already exist before this
  #        'inotifywait', since the '/vagrant' directory will already have been
  #        mounted on the initial build.
  #
  #  Note: every 'command' implementation checks if directory is nonempty, then
  #        touch all files in the directory, respectively.
  exec {"touch-${directory_src[$index]}-files":
    command => "if [ 'ls -A /vagrant/src/${directory_src[$index]}/' ]; then touch /vagrant/src/${directory_src[$index]}/*; fi",
    refreshonly => true,
    provider => shell,
  }
}