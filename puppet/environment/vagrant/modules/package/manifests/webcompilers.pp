### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::webcompilers {
    ## hiera attributes
    $hiera_dev          = lookup('development')
    $version_uglify_js  = $hiera_dev['npm']['uglify-js']
    $version_imagemin   = $hiera_dev['npm']['imagemin']
    $version_node_sass  = $hiera_dev['npm']['node-sass']
    $version_babel_core = $hiera_dev['npm']['babel-core']
    $version_browserify = $hiera_dev['npm']['browserify']
    $version_babelify   = $hiera_dev['npm']['babelify']

    ## variables
    $webcompilers = [
        "uglify-js@${version_uglify_js}",
        "imagemin@${$version_imagemin}",
        "node-sass@${$version_node_sass}",
        "babel-core@${$version_babel_core}",
        "browserify@${$version_browserify}",
        "babelify@${version_babelify}"
    ]

    ## packages: install general packages (npm)
    package { $webcompilers:
        ensure   => 'present',
        provider => 'npm',
    }
}