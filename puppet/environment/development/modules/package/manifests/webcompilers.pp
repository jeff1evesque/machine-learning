### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::webcompilers {
    $webcompilers = [
        'uglify-js',
        'imagemin',
        'node-sass',
        'babel-core',
        'browserify',
        'babelify'
    ]

    ## packages: install general packages (npm)
    package { $webcompilers:
        ensure   => 'present',
        provider => 'npm',
        require  => Class['nodejs'],
    }
}