### Note: the prefix 'compiler::::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::initial_compile {
    $sources = [
        'jsx',
        'img',
        'scss',
        'js'
    ]

    $sources.each |String $source| {
        ## variables
        $check_files = "if [ \"$(ls -A /vagrant/src/${source}/)\" ];"
        $touch_files = "then touch /vagrant/src/${source}/*; fi"

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
        exec { "touch-${source}-files":
            command     => "${check_files} ${touch_files}",
            refreshonly => true,
            provider    => shell,
        }
    }
}