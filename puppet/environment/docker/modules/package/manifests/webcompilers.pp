###
### webcompilers.pp, install webcompiler packages.
###
class package::webcompilers {
    include package::nodejs

    ## hiera attributes
    $hiera_dev          = lookup('development')
    $version_uglify_js  = $hiera_dev['npm']['specific']['uglify-js']
    $version_imagemin   = $hiera_dev['npm']['specific']['imagemin']
    $version_node_sass  = $hiera_dev['npm']['specific']['node-sass']
    $version_babel_core = $hiera_dev['npm']['specific']['babel-core']
    $version_browserify = $hiera_dev['npm']['specific']['browserify']
    $version_babelify   = $hiera_dev['npm']['specific']['babelify']

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
        require  => Class['package::nodejs'],
    }
}