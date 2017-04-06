###
### init.pp: install general packages.
###

class package {
    require apt

    ## local variables
    $packages = lookup('development')

    ## iterate 'packages' hash
    $packages.each|String $provider| {
        if ($provider in ['apt', 'npm', 'pip']) {
            $provider['general'].each|String $package, String $version| {
                package { $package:
                    ensure   => $version,
                    provider => $provider,
                }
            }
        }
    }
}
