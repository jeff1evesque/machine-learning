###
### dependency.pp, ensure directories.
###
class browserify::dependency {
    ## local variables
    $root_dir    = $::browserify::root_dir
    $directories = [
        "${root_dir}/log",
        "${root_dir}/log/webcompiler",
    ]

    ## log directories
    file { $directories:
        ensure   => 'directory',
        mode     => '0755',
        owner    => 'root',
        group    => 'root',
    }

    ## source + asset directories
    file { "${root_dir}/src/jsx":
        ensure => 'directory',
        mode     => '0755',
        owner    => 'root',
        group    => 'root',
    }
    file { "${root_dir}/src/js":
        ensure => 'directory',
        mode     => '0755',
        owner    => 'root',
        group    => 'root',
    }

    ## create node directory
    file { "${root_dir}/src/node_modules":
        ensure => 'directory',
        owner  => root,
        group  => root,
        mode   => '0755',
    }
}
