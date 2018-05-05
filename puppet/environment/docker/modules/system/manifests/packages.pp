###
### packages.pp, install general packages.
###
class system::packages {
    contain apt
    contain python

    ## local variables
    $packages = $::system::packages

    ## iterate 'packages' hash
    if $packages {
        $packages.each |String $provider, $providers| {
            if ($provider in ['apt', 'npm', 'pip']) {
                if has_key($providers, 'general') {
                    $providers['general'].each|String $package, String $version| {
                        package { $package:
                            ensure   => $version,
                            provider => $provider,
                            require  => [
                                Class['apt'],
                                Class['python'],
                            ],
                        }
                    }
                }
            }
        }
    }
}