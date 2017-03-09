###
### xmltodict.pp, install package.
###
class package::xmltodict {
    include python
    include package::nodejs

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['xmltodict']

    package { 'xmltodict':
        ensure   => $version,
        provider => 'pip',
        require  => Class['package::nodejs'],
    }
}