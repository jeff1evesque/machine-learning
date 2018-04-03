###
### webcompilers.pp, install webcompiler packages.
###
class package::webcompilers {
    include package::nodejs

    ## hiera attributes
    $hiera              = lookup('development')
    $version_uglify_js  = $hiera['npm']['custom']['uglify-js']
    $version_node_sass  = $hiera['npm']['custom']['node-sass']
    $version_babel_core = $hiera['npm']['custom']['babel-core']
    $version_browserify = $hiera['npm']['custom']['browserify']
    $version_babelify   = $hiera['npm']['custom']['babelify']

    ## variables
    $webcompilers = [
        "uglify-js@${version_uglify_js}",
        "babel-core@${version_babel_core}",
        "browserify@${version_browserify}",
        "babelify@${version_babelify}",
    ]

    ## packages: install general packages (npm)
    package { $webcompilers:
        ensure   => 'present',
        provider => 'npm',
        require  => Class['package::nodejs'],
    }

    ## 'docker build' workaround (i.e. sass.dockerfile)
    exec { "node-sass@${version_node_sass}":
        command  => "npm install -g node-sass@${version_node_sass}",
        unless   => 'which node-sass',
        path     => '/usr/bin',
        require  => Class['package::nodejs'],
    }
}