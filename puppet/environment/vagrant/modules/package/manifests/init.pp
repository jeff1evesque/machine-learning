###
### init.pp: install general packages.
###

class package {
    include apt
    include python
    include package::nodejs
    include package::python_dev

    ## local variables
    $packages = lookup('development')

    ## iterate 'packages' hash
    $packages.each |String $provider, $providers| {
        notify { "provider: ${provider}": }
        notify { "providers: ${providers}": }
        if ($provider in ['apt', 'npm', 'pip']) {
            $providers['general'].each|String $package, String $version| {
                package { $package:
                    ensure   => $version,
                    provider => $provider,
                    require  => [
                        Class['apt'],
                        Class['python'],
                        Class['package::nodejs'],
                        Class['package::python_dev']
                    ],
                }
            }
        }
    }
}
