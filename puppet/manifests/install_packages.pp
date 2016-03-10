## define $PATH for all execs, and packages
Exec {
  path => ['/usr/bin/', '/bin/', '/usr/local', '/usr/sbin/', '/sbin/'],
}

## include puppet modules: this (also) runs 'apt-get update'
include python
include apt

class application_packages {
    $packages_general_pip = [
        'jsonschema',
        'xmltodict',
        'six'
    ]

    ## packages: install general packages (pip)
    package { $packages_general_pip:
        ensure   => 'installed',
        provider => 'pip',
    }
}

## constructor
class constructor {
    contain application_packages
}
include constructor