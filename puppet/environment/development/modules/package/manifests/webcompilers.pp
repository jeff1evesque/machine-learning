### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::webcompilers {
    ## variables
    $webcompilers = [
        'uglify-js@2.6.2',
        'imagemin@4.0.0',
        'node-sass@3.4.2',
        'babel-core@6.7.4',
        'browserify@13.0.0',
        'babelify@7.2.0'
    ]

    ## packages: install general packages (npm)
    package { $webcompilers:
        ensure   => 'present',
        provider => 'npm',
    }
}