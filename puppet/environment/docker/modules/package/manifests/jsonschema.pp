### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
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