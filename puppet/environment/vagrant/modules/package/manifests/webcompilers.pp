### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::webcompilers {
    ## hiera attributes
    $hiera_dev          = hiera('development')
    $version_uglify_js  = $hiera_dev['pip']['uglify-js']
    $version_imagemin   = $hiera_dev['pip']['imagemin']
    $version_node_sass  = $hiera_dev['pip']['node-sass']
    $version_babel_core = $hiera_dev['pip']['babel-core']
    $version_browserify = $hiera_dev['pip']['browserify']
    $version_babelify   = $hiera_dev['pip']['babelify']

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