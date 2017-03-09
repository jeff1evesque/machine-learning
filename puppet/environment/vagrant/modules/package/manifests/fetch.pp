###
### fetch.pp, install package.
###
class package::fetch {
    include package::nodejs

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['npm']['fetch']

    ## package: install general packages (npm)
    package { "whatwg-fetch@${version}":
        ensure   => 'present',
        provider => 'npm',
        require  => Class['package::nodejs'],
    }
}