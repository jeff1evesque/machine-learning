## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## variables
$compilers = ['uglifyjs', 'sass', 'imagemin']
$directory = ['css', 'js', 'img']

## dynamically create compilers
$compilers.each |Integer $index, String $compiler| {
    ## webcompiler(s)
    if ($compiler == 'uglifyjs' {
        $webcompimler = <<EOT
            # filename (without 'last' extension)
            filename="\${file}"
        EOT
    }
	elsif ($compiler == 'sass' {
        $webcompiler = <<EOT
            # filename (without 'last' extension)
            filename="\${file%.*}"

            # compile with 'sass'
            sass /src/scss/"$file" /web_interface/static/css/"\$filename".min.css --style compressed
        EOT
	}
    elsif ($compiler == 'imagemin') {
        $webcompiler = <<EOT
            # filename (without directory path)
            filename="\${file##*/}"
            file_extension="\${file##*.}"

            # minify with 'imagemin'
            if [ "\$file_extension" = 'gif' ]; then
                cp /src/img/"\$file" /web_interface/static/img/"\$filename"
            else
                imagemin /src/img/"\$file" > /web_interface/static/img/"\$filename"
            fi
        EOT
	}

    ## create asset directories
    file {"/vagrant/web_interface/static/${directory[$index]}/":
        ensure => 'directory',
        before => File["${compiler}-startup-script"],
    }

    ## create startup script (heredoc syntax)
    #
    #  @("EOT"), the use double quotes on the end tag, allows variable interpolation within the puppet heredoc.
    #
    #  Note: the '/vagrant/log/' directory is created in 'start_webserver.pp'.
    #
    #  Note: the dash in closing heredoc tag, removes any trailing whitespace, or newline on the last line of
    #        the heredoc string.
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
                   #  @filename, @file_extension, the assignment value is escaped, since it is contained within
                   #       the puppet heredoc
                   script
                   # track execution of script
                   set -x; exec > /vagrant/log/${compiler}_execution.log 2>&1

                   # watch '/web-interface/static/${directory[$index]}' subdirectory
                   inotifywait /web-interface/static/${directory[$index]} -m -e close_write -e move -e create |
                       # Compile ${directory[$index]}
                       while read path action file; do

                       ${webcompiler}
                       done
                   end script

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
                   |- EOT
               notify  => Exec["dos2unix-${compiler}"],
        }

    ## convert clrf (windows to linux) in case host machine is windows.
    #
    #  @notify, ensure the webserver service is started. This is similar to an exec statement, where the
    #      'refreshonly => true' would be implemented on the corresponding listening end point. But, the
    #      'service' end point does not require the 'refreshonly' attribute.
    exec {"dos2unix-${compiler}":
        command => "dos2unix /etc/init/${compiler}.conf",
        refreshonly => true,
        notify => Service["${compiler}"],
    }

    ## start ${compiler} service
    service {"${compiler}":
        ensure => 'running',
        enable => 'true',
    }
}