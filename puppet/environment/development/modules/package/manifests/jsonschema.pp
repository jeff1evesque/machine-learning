### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::jsonschema {
    include python

    package { 'jsonschema':
        ensure   => 'installed',
        provider => 'pip',
    }
}