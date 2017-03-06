##
## xmltodict.pp, install package.
##
class package::xmltodict {
    include python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['xmltodict']

    package { 'xmltodict':
        ensure   => $version,
        provider => 'pip',
    }
}