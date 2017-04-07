###
### init.pp: install general packages.
###

class package {
    require apt
    require python
    include package::nodejs
    include package::python_dev

    ## local variables
    $packages = lookup('development')

    ## iterate 'packages' hash
    $packages.each|$provider| {
        if ($provider in ['apt', 'npm', 'pip']) {
            $provider['general'].each|String $package, String $version| {
                package { $package:
                    ensure   => $version,
                    provider => $provider,
                    require  => [
                        Class['package::nodejs'],
                        Class['package::python_dev']
                    ],
                }
            }
        }
    }
}
contain package