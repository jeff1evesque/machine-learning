###
### jsonschema.pp, install package.
###
class package::jsonschema {
    include python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['jsonschema']

    package { 'jsonschema':
        ensure   => $version,
        provider => 'pip',
    }
}