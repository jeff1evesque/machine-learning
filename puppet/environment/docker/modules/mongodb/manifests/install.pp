###
### install.pp, install single mongodb instance.
###
class mongodb::install {
    ## local variables
    $keyserver           = $::mongodb::keyserver
    $mongodb_key         = $::mongodb::mongodb_key
    $mongodb_source_list = $::mongodb::mongodb_source_list

    ## https://docs.mongodb.com/v4.0/tutorial/install-mongodb-on-ubuntu/
    exec { 'apt-key-puppetlabs':
        command => "apt-key adv --keyserver ${keyserver} --recv ${mongodb_key}",
        unless  => "apt-key list | grep ${mongodb_key}",
        before  => File['mongodb-list-file'],
        path    => ['/usr/bin', '/bin'],
    }

    file { 'mongodb-list-file':
        path    => '/etc/apt/sources.list.d/mongodb-org-4.0.list',
        content => $mongodb_source_list,
        require => Exec['apt-key-puppetlabs'],
        notify  => Exec['apt-get-update'],
    }

    exec { 'apt-get-update':
        command     => 'apt-get update',
        path        => ['/usr/bin', '/bin'],
        before      => Package['mongodb-org-server'],
        refreshonly => true,
    }

    package { 'mongodb-org-server':
        ensure  => installed,
    }

    package { 'mongodb-org-shell':
        ensure => installed,
    }
}