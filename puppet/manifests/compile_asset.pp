## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/', '/sbin/', '/bin/', '/usr/share/']}

## variables
#
#  @asset_dir, indicate whether to create corresponding asset directory.
#
#  @src_dir, indicate whether to create corresponding source directory.
#
#  Note: hash iteration is done alphabetically.
$compilers = {
    browserify => {
        src       => 'jsx',
        asset     => 'js',
        asset_dir => true,
        src_dir   => true,
    },
    imagemin   => {
        src   => 'img',
        asset => 'img',
        asset_dir => true,
        src_dir   => true,
    },
    sass       => {
        src       => 'scss',
        asset     => 'css',
        asset_dir => true,
        src_dir   => true,
    },
    uglifyjs   => {
        src       => 'js',
        asset     => 'js',
        asset_dir => false,
        src_dir   => false,
    }
}

## create compilers
class create_compilers {
    ## dynamically create compilers
    $compilers.each |String $compiler, Hash $resource| {
        ## variables
        $check_files = "if [ \"$(ls -A /vagrant/src/${resource['src']}/)\" ];"
        $touch_files = "then touch /vagrant/src/${resource['src']}/*; fi"

        ## create asset directories (if not exist)
        if ($resource['asset_dir']) {
            file {"/vagrant/interface/static/${resource['asset']}/":
                ensure => 'directory',
                before => File["${compiler}-startup-script"],
            }
        }

        ## create src directories (if not exist)
        if ($resource['src_dir']) {
            file {"/vagrant/src/${resource['src']}/":
                ensure => 'directory',
                before => File["${compiler}-startup-script"],
            }
        }

        ## create startup script: for webcompilers, using puppet templating
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
            notify => Exec["touch-${resource['src']}-files"],
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
        exec {"touch-${resource['src']}-files":
            command     => "${check_files} ${touch_files}",
            refreshonly => true,
            provider    => shell,
        }
    }
}

## constructor
class constructor {
    contain create_compilers
}
include constructor