###
### install.pp, install sass
###
class sass::dependency {
    ## local variables
    $node_version       = $::sass::node_version
    $node_sass_version  = $::sass::node_sass_version
    $root_dir           = $::sass::root_dir
    $directories        = [
        "${root_dir}/log",
        "${root_dir}/log/webcompiler",
    ]

    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => $node_version,
    }

    ## install node-sass
    package { 'node-sass': 
        ensure          => $node_sass_version
    }
}
