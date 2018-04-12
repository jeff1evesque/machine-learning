###
### config.pp, configure node-sass
###
class sass::config {
    ## local variables
    $root_dir     = $::sass::root_dir
    $root_puppet  = $::sass::root_puppet
    $compiler_dir = "${root_puppet}/code/modules/sass/scripts"

    ## dos2unix line endings
    file { "${compiler_dir}/sass":
        ensure    => file,
        content   => dos2unix(template("${compiler_dir}/sass")),
        mode      => '0644',
        owner     => 'root',
        group     => 'root',
    }

    ## source + asset directories
    file { "${root_dir}/src/scss":
        ensure    => 'directory',
        mode      => '0755',
        owner     => 'root',
        group     => 'root',
    }
    file { "${root_dir}/interface/static/css":
        ensure    => 'directory',
        mode      => '0755',
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
