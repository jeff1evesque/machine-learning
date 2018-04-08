###
### install.pp, install uglifyjs
###
class uglifyjs::install {
    ## local variables
    $node_version       = $::uglifyjs::node_version
    $uglifyjs_version   = $::uglifyjs::uglifyjs_version
    $root_dir           = $::uglifyjs::root_dir
    $directories        = [
        "${root_dir}/log",
        "${root_dir}/log/webcompiler",
    ]

    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => $node_version,
    }

    ## install uglifyjs related compilers
    package { 'uglify-js':
        ensure          => $node_uglifyjs_version,
        provider        => 'npm',
        require         => Class['nodejs'],
    }
}
