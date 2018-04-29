###
### config.pp, configure nginx.
###
class reverse_proxy::config {
    ## local variables
    $yaml               = $::reverse_proxy::yaml
    $type               = $::reverse_proxy::type
    $self_signed        = $::reverse_proxy::self_signed
    $vhost              = $::reverse_proxy::vhost
    $listen_port        = $::reverse_proxy::listen_port
    $members            = $::reverse_proxy::members
    $proxy              = $::reverse_proxy::proxy
    $cert_path          = $::reverse_proxy::cert_path
    $pkey_path          = $::reverse_proxy::pkey_path
    $cert_country       = $::reverse_proxy::cert_country
    $cert_org           = $::reverse_proxy::cert_org
    $cert_state         = $::reverse_proxy::cert_state
    $cert_locality      = $::reverse_proxy::cert_locality
    $cert_unit          = $::reverse_proxy::cert_unit
    $cert_bit           = $::reverse_proxy::cert_bit
    $cert_days          = $::reverse_proxy::cert_days
    $access_log         = $::reverse_proxy::access_log
    $error_log          = $::reverse_proxy::error_log

    ## hiera already array
    if $yaml and $members {
        $split_members  = $members
    }

    ## convert module argument to array
    elsif $members {
        $split_members  = split($members, ',')
    }

    ## reverse proxy members
    if $split_members {
        nginx::resource::upstream { "${proxy}-${type}":
            ensure      => present,
            members     => $split_members,
        }
    }

    ## https only server: since 'listen_port' = 'ssl_port'
    nginx::resource::server { $vhost:
        proxy           => "http://${proxy}-${type}",
        ssl             => true,
        ssl_cert        => "${cert_path}/${vhost}.crt",
        ssl_key         => "${pkey_path}/${vhost}.key",
        listen_port     => $listen_port,
        ssl_port        => $listen_port,
        access_log      => $access_log,
        error_log       => $error_log,
    }

    ## create ssl certificate
    if $self_signed {
        file { '/root/build':
            ensure      => 'directory',
            owner       => 'root',
            group       => 'root',
            mode        => '0700',
        }

        file { "/root/build/ssl-nginx-${type}":
            ensure      => present,
            content     => dos2unix(template('reverse_proxy/ssl.erb')),
            owner       => 'root',
            group       => 'root',
            mode        => '0700',
            require     => File['/root/build'],
            notify      => Exec["create-certificate-${type}"],
        }

        exec { "create-certificate-${type}":
            command     => "./ssl-nginx-${type}",
            cwd         => '/root/build',
            path        => '/usr/bin',
            provider    => shell,
            refreshonly => true,
        }
    }

    else {
        notify {'Please remember to provide your own certificate!':}
    }
}
