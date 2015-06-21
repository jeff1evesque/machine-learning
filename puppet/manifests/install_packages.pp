## variables
case $::osfamily {
    'redhat': {
        $packages_general = ['inotify-tools', 'python-pip', 'ruby-devel']
    }
    'debain': {
        $packages_general = ['inotify-tools', 'python-pip', 'ruby-dev']
    }
    default: {

    }
}

## packages: install general packages (apt)
package {$packages_general_apt:
    ensure => 'installed',
}
