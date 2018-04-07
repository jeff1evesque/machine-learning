###
### config.pp, configure sass.
###
class browserify::dependency {
    ## local variables
    $root_dir     = $::browserify::root_dir
    $root_puppet  = $::browserify::root_puppet
    $compiler_dir = "${root_puppet}/code/modules/browserify/scripts"
    $user         = $::browserify::user
    $group        = $::browserify::group
    $log_path     = "${root_dir}/log/webcompiler"

    ## dos2unix line endings
    file { "/etc/init/browserify.conf":
        ensure    => file,
        content   => dos2unix(template('compiler/webcompilers.erb')),
        mode      => '0644',
        owner     => 'root',
        group     => 'root',
    }

    ## dos2unix line endings
    file { "${compiler_dir}/browserify.conf":
        ensure    => file,
        content   => dos2unix(template("${root_puppet}/code/modules/browserify/scripts/browserify")),
        mode      => '0644',
        owner     => 'root',
        group     => 'root',
    }

    ## create node directory
    file { "${root_dir}/src/node_modules":
        ensure    => 'directory',
        owner     => root,
        group     => root,
        mode      => '0755',
    }
}
