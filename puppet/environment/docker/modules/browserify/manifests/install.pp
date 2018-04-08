###
### install.pp, install browserify
###
class browserify::install {
    ## local variables
    $node_version       = $::browserify::node_version
    $browserify_version = $::browserify::browserify_version
    $babel_core_version = $::browserify::babel_core_version
    $babelify_version   = $::browserify::babelify_version
    $root_dir           = $::browserify::root_dir
    $directories        = [
        "${root_dir}/log",
        "${root_dir}/log/webcompiler",
    ]
    $node_packages      = $::browserify::node_packages

    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => $node_version,
    }

    ## install browserify related compilers
    package { 'babel-core': 
        ensure          => $babel_core_version,
        provider        => 'npm',
        require         => Class['nodejs'],
    }

    package { 'babelify': 
        ensure          => $babelify_version
        provider        => 'npm',
        require         => Class['nodejs'],
    }

    package { 'browserify': 
        ensure          => $node_browserify_version,
        provider        => 'npm',
        require         => Class['nodejs'],
    }

    ## install 'package.json'
    if $node_packages {
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
}
