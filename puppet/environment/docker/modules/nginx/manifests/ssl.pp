###
### ssl.pp, configure ssl certificates required by nginx.
###
class nginx::ssl {
    include system::build_directory

    ## local variables
    $hiera             = lookup('reverse_proxy')
    $nginx_type        = $hiera('type')
    $vhost             = $hiera['vhost']
    $cert              = $hiera['certificate']
    $cert_path         = $cert['cert_path']
    $pkey_path         = $cert['pkey_path']
    $cert_name         = $cert['name']
    $cert_country      = $cert['props']['country']
    $cert_org          = $cert['props']['organization']
    $cert_state        = $cert['props']['state']
    $cert_locality     = $cert['props']['locality']
    $cert_unit         = $cert['props']['unit']
    $cert_bit          = $cert['props']['bit']
    $cert_days         = $cert['props']['days']

    ## create ssl certificate
    file { "/root/build/ssl-nginx-${nginx_type}":
        ensure         => present,
        content        => dos2unix(template("webserver/ssl-${nginx_type}.erb")),
        owner          => 'root',
        group          => 'root',
        mode           => '0700',
        require        => File['/root/build'],
        notify         => Exec["create-ssl-certificate-${nginx_type}"],
    }

    exec { "create-ssl-certificate-${nginx_type}":
        command        => "./ssl-nginx-${nginx_type}",
        cwd            => '/root/build',
        path           => '/usr/bin',
        provider       => shell,
        refreshonly    => true,
    }
}
