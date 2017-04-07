###
### pyyaml.pp, install package.
###
class package::pyyaml {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['custom']['pyyaml']

    package { 'pyyaml':
        ensure   => $version,
        provider => 'pip',
    }
}