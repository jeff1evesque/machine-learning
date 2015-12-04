## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/', '/sbin/', '/bin/', '/usr/share/']}

## variables: the order of the following array variables are important
$compilers = {
    uglifyjs   => {
        src   => 'js',
        asset => 'asset'
    },
    browserify => {
        src  => 'jsx',
        asset => 'js'
    },
    sass       => {
        src   => 'scss',
        asset => 'css'
    },
    imagemin   => {
        src   => 'img',
        asset => 'img'
    }
}

## dynamically create compilers
$compilers.each |String $index, Hash $compiler| {
    ## variables
    $check_files = "if [ 'ls -A /vagrant/src/${compiler['src']}/' ];"
    $touch_files = "then touch /vagrant/src/${compiler['src']}/*; fi"

    ## create asset directories
    file {"/vagrant/interface/static/${compiler['asset']}/":
        ensure => 'directory',
        before => File["${compiler}-startup-script"],
    }

    ## create startup script: for webcompilers, using heredoc syntax
    file {"${compiler}-startup-script":
        path    => "/etc/init/${compiler}.conf",
        ensure  => 'present',
        content => template('/vagrant/puppet/template/webcompilers.erb'),
        notify  => Exec["dos2unix-upstart-${compiler}"],
    }

    ## dos2unix upstart: convert clrf (windows to linux) in case host machine
    #                    is windows.
    #
    #  @notify, ensure the webserver service is started. This is similar to an
    #      exec statement, where the 'refreshonly => true' would be implemented
    #      on the corresponding listening end point. But, the 'service' end
    #      point does not require the 'refreshonly' attribute.
    exec {"dos2unix-upstart-${compiler}":
        command     => "dos2unix /etc/init/${compiler}.conf",
        refreshonly => true,
        notify      => Exec["dos2unix-bash-${compiler}"],
    }

    ## dos2unix bash: convert clrf (windows to linux) in case host machine is
    #                 windows.
    #
    #  @notify, ensure the webserver service is started. This is similar to an
    #      exec statement, where the 'refreshonly => true' would be implemented
    #      on the corresponding listening end point. But, the 'service' end
    #      point does not require the 'refreshonly' attribute.
    exec {"dos2unix-bash-${compiler}":
        command     => "dos2unix /vagrant/puppet/scripts/${compiler}",
        refreshonly => true,
        notify      => Service[$compiler],
    }

    ## start ${compiler} service
    service {$compiler:
        ensure => 'running',
        enable => true,
        notify => Exec["touch-${compiler['src']}-files"],
    }

    ## touch source: ensure initial build compiles every source file.
    #
    #  @touch, changes the modification time to the current system time.
    #
    #  Note: the current inotifywait implementation watches close_write, move,
    #        and create. However, the source files will already exist before
    #        this 'inotifywait', since the '/vagrant' directory will already
    #        have been mounted on the initial build.
    #
    #  Note: every 'command' implementation checks if directory is nonempty,
    #        then touch all files in the directory, respectively.
    exec {"touch-${compiler['src']}-files":
        command     => "${check_files}${touch_files}",
        refreshonly => true,
        provider    => shell,
    }
}