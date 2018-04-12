###
### install.pp, install sass
###
class sass::install {
    ## local variables
    $node_version       = $::sass::node_version
    $node_sass_version  = $::sass::node_sass_version

    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => $node_version,
    }

    ## install node-sass
    package { 'node-sass': 
        ensure          => $node_sass_version,
        provider        => 'npm',
        require         => Class['nodejs'],
    }
}
