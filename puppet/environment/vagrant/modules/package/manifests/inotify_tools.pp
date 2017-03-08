###
### inotify_tools.pp, install package.
###
class package::inotify_tools {
    include package::nodejs

    ## update apt-get
    require apt

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['apt']['inotify-tools']

    package { "inotify-tools=${version}":
        ensure  => 'installed',
        require => Class['package::nodejs'],
    }
}