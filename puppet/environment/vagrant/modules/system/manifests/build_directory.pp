###
### build_directory.pp, create 'build/' directory.
###
class system::build_directory {
    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    file { "${root_dir}/build/":
        ensure => 'directory',
    }

    file { '/root/build':
      ensure => directory,
      mode   => '0700',
      owner  => 'root',
      group  => 'root',
    }
}