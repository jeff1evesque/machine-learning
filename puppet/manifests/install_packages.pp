## variables
case $::osfamily {
    'redhat': {
        $packages_general_apt = ['inotify-tools', 'python-pip', 'ruby-devel']
    }
    'debain': {
        $packages_general_apt = ['inotify-tools', 'python-pip', 'ruby-dev']
    }
    default: {
        $packages_general_gem = ['librarian-puppet']
    }
}

## packages: install general packages (apt)
package {$packages_general_apt:
    ensure => 'installed',
}

## packages: install general packages (gem)
package {$packages_general_gem:
    ensure => 'installed',
}
