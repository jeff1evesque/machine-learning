###
### webcompilers.pp, install webcompiler packages.
###
class package::webcompilers {
    include package::nodejs

    ## hiera attributes
    $hiera              = lookup('development')
    $version_uglify_js  = $hiera['npm']['custom']['uglify-js']

    ## variables
    $webcompilers = [
        "uglify-js@${version_uglify_js}",
    ]

    ## packages: install general packages (npm)
    package { $webcompilers:
        ensure   => 'present',
        provider => 'npm',
        require  => Class['package::nodejs'],
    }
}