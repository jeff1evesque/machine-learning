###
### ssl.pp, configure ssl certificates required by nginx.
###
class webserver::ssl {
    ## variables
    $hiera_webserver     = lookup('webserver')
    $nginx               = $hiera_webserver['nginx']
    $nginx_reverse_proxy = $nginx['reverse_proxy']
    $nginx_vhost         = $nginx_reverse_proxy['vhost']
    $nginx_cert          = $nginx['certificate']
    $nginx_cert_path     = $nginx_cert['cert_path']
    $nginx_pkey_path     = $nginx_cert['pkey_path']
    $nginx_cert_name     = $nginx_cert['name']
    $nginx_cert_country  = $nginx_cert['props']['country']
    $nginx_cert_org      = $nginx_cert['props']['organization']
    $nginx_cert_state    = $nginx_cert['props']['state']
    $nginx_cert_locality = $nginx_cert['props']['locality']
    $nginx_cert_unit     = $nginx_cert['props']['unit']
    $nginx_cert_bit      = $nginx_cert['props']['bit']
    $nginx_cert_days     = $nginx_cert['props']['days']

    ## create ssl certificate
    exec { 'chage-pass':
      command     => dos2unix(template('webserver/ssl.erb')),
      unless      => [
        "test -f ${nginx_cert_path}/${vhost}.crt",
        "test -f ${nginx_pkey_path}/${vhost}.key",
      ],
      path        => '/usr/bin',
      provider    => shell,
    }
}