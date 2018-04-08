###
### config.pp, configure uglifyjs.
###
class uglifyjs::dependency {
    ## local variables
    $root_dir     = $::uglifyjs::root_dir
    $root_puppet  = $::uglifyjs::root_puppet
    $compiler_dir = "${root_puppet}/code/modules/uglifyjs/scripts"
    $user         = $::uglifyjs::user
    $group        = $::uglifyjs::group
    $log_path     = "${root_dir}/log/webcompiler"

    ## dos2unix line endings
    file { "/etc/init/uglifyjs.conf":
        ensure    => file,
        content   => dos2unix(template('compiler/webcompilers.erb')),
        mode      => '0644',
        owner     => 'root',
        group     => 'root',
    }

    ## dos2unix line endings
    file { "${compiler_dir}/uglifyjs.conf":
        ensure    => file,
        content   => dos2unix(template("${root_puppet}/code/modules/uglifyjs/scripts/uglifyjs")),
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
