###
### init.pp: install general packages.
###

class package {
    include apt
    include python
    include package::nodejs
    include package::python_dev

    ## local variables
    $packages      = lookup('development')
    $hiera_general = lookup('general')
    $node_packages = lookup('dependencies')
    $root_dir      = $hiera_general['root']

    ## iterate 'packages' hash
    $packages.each |String $provider, $providers| {
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

    ## create node directory
    file { "${root_dir}/src/node_modules":
        ensure => 'directory',
        owner  => root,
        group  => root,
        mode   => '0755',
    }

    ## iterate 'package.json'
    $node_packages.each|String $package, String $version| {
        nodejs::npm { "install-${package}":
            ensure          => $version,
            package         => $package,
            install_options => '--no-bin-links',
            target          => "${root_dir}/src/node_modules",
        }
    }
}
