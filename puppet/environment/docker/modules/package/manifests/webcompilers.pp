###
### webcompilers.pp, install webcompiler packages.
###
class package::webcompilers {
    include package::nodejs

    ## hiera attributes
    $hiera_dev          = lookup('development')
    $version_uglify_js  = $hiera_dev['npm']['custom']['uglify-js']
    $version_node_sass  = $hiera_dev['npm']['custom']['node-sass']
    $version_babel_core = $hiera_dev['npm']['custom']['babel-core']
    $version_browserify = $hiera_dev['npm']['custom']['browserify']
    $version_babelify   = $hiera_dev['npm']['custom']['babelify']

    ## variables
    $webcompilers = [
        "uglify-js@${version_uglify_js}",
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