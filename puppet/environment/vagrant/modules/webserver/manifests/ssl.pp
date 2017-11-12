###
### ssl.pp, configure ssl certificates required by nginx.
###
class webserver::ssl {
    include system::build_directory

    ## variables
    $hiera_webserver     = lookup('webserver')
    $nginx_web           = $hiera_webserver['nginx_web']
    $reverse_proxy_web   = $nginx_web['reverse_proxy']
    $vhost_web           = $reverse_proxy_web['vhost']
    $cert_web            = $nginx_web['certificate']
    $cert_path_web       = $cert_web['cert_path']
    $pkey_path_web       = $cert_web['pkey_path']
    $cert_name_web       = $cert_web['name']
    $cert_country_web    = $cert_web['props']['country']
    $cert_org_web        = $cert_web['props']['organization']
    $cert_state_web      = $cert_web['props']['state']
    $cert_locality_web   = $cert_web['props']['locality']
    $cert_unit_web       = $cert_web['props']['unit']
    $cert_bit_web        = $cert_web['props']['bit']
    $cert_days_web       = $cert_web['props']['days']

    $nginx_api           = $hiera_webserver['nginx_api']
    $reverse_proxy_api   = $nginx_api['reverse_proxy']
    $vhost_api           = $reverse_proxy_api['vhost']
    $cert_api            = $nginx_api['certificate']
    $cert_path_api       = $cert_api['cert_path']
    $pkey_path_api       = $cert_api['pkey_path']
    $cert_name_api       = $cert_api['name']
    $cert_country_api    = $cert_api['props']['country']
    $cert_org_api        = $cert_api['props']['organization']
    $cert_state_api      = $cert_api['props']['state']
    $cert_locality_api   = $cert_api['props']['locality']
    $cert_unit_api       = $cert_api['props']['unit']
    $cert_bit_api        = $cert_api['props']['bit']
    $cert_days_api       = $cert_api['props']['days']

    ## web-interface: create ssl certificate
    file { '/root/build/ssl-nginx-web':
      ensure  => present,
      content => dos2unix(template('webserver/ssl-web.erb')),
      owner   => 'root',
      group   => 'root',
      mode    => '0700',
      require => File['/root/build'],
      notify  => Exec['create-ssl-certificate-web'],
    }

    exec { 'create-ssl-certificate-web':
      command     => './ssl-nginx-web',
      cwd         => '/root/build',
      path        => '/usr/bin',
      provider    => shell,
      refreshonly => true,
    }

    ## programmatic-interface: create ssl certificate
    file { '/root/build/ssl-nginx-api':
      ensure  => present,
      content => dos2unix(template('webserver/ssl-api.erb')),
      owner   => 'root',
      group   => 'root',
      mode    => '0700',
      require => File['/root/build'],
      notify  => Exec['create-ssl-certificate-api'],
    }

    exec { 'create-ssl-certificate-api':
      command     => './ssl-nginx-api',
      cwd         => '/root/build',
      path        => '/usr/bin',
      provider    => shell,
      refreshonly => true,
    }
}
