###
### config.pp, configure node-sass
###
class sass::dependency {
    ## local variables
    $root_dir              = $::sass::root_dir
    $root_puppet           = $::sass::root_puppet
    $compiler_dir          = "${root_puppet}/code/modules/sass/scripts"
    $user                  = $::sass::user
    $group                 = $::sass::group
    $log_path              = "${root_dir}/log/webcompiler"

    ## dos2unix line endings
    file { "/etc/init/sass.conf":
        ensure  => file,
        content => dos2unix(template('compiler/webcompilers.erb')),
        mode    => '0644',
        owner   => 'root',
        group   => 'root',
    }

    ## dos2unix line endings
    file { "${compiler_dir}/sass.conf":
        ensure  => file,
        content => dos2unix(template('/etc/puppetlabs/code/modules/sass/scripts/sass')),
        mode    => '0644',
        owner   => 'root',
        group   => 'root',
    }
}
