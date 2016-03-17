### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::webcompilers {
    ## variables
    $webcompilers = [
        'uglify-js',
        'imagemin',
        'node-sass',
        'babel-core',
        'browserify',
        'babelify'
    ]

    ## print node / npm version
    exec { 'echo-general-notice':
        command => 'echo "installing npm packages with: "',
        path => '/bin',
        notify => Exec['echo-versions'],
        logoutput => true,
    }
    exec { 'echo-versions':
        command => 'npm -v && node -v',
        path    => '/usr/bin',
        refreshonly => true,
        before  => Package[$webcompilers],
        logoutput => true,
    }

    ## packages: install general packages (npm)
    package { $webcompilers:
        ensure   => 'present',
        provider => 'npm',
    }
}