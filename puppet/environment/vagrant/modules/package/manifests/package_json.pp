###
### package_json.pp, install necessary webpackages defined in 'package.json'.
###
class package::package_json {
    include package::nodejs

    ## local variables
    $node_packages = lookup('dependencies')
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

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
            install_options => ['--no-bin-links'],
            target          => "${root_dir}/src/node_modules",
            require         => [
                Class['package::nodejs'],
                File["${root_dir}/src/node_modules"],
            ]
        }
    }
}