###
### packages.pp, install general packages.
###
class system::packages {
    contain apt

    ## local variables
    $packages = $::system::packages

    ## iterate 'packages' hash
    if $packages {
        $packages.each |String $provider, $providers| {
            if ($provider in ['apt', 'pip3']) {
                if has_key($providers, 'general') {
                    $providers['general'].each|String $package, String $version| {
                        package { $package:
                            ensure   => $version,
                            provider => $provider,
                            require  => [
                                Class['apt'],
                            ],
                        }
                    }
                }
            }
        }
    }
}
