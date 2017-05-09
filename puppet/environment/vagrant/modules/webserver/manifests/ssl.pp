###
### ssl.pp, configure ssl certificates required by nginx.
###
class webserver::ssl {
    ## variables
    $hiera_webserver = lookup('webserver')
    $nginx           = $hiera_webserver['nginx']
    $reverse_proxy   = $nginx['reverse_proxy']
    $vhost           = $reverse_proxy['vhost']
    $cert            = $nginx['certificate']
    $cert_path       = $cert['cert_path']
    $pkey_path       = $cert['pkey_path']
    $cert_name       = $cert['name']
    $cert_country    = $cert['props']['country']
    $cert_org        = $cert['props']['organization']
    $cert_state      = $cert['props']['state']
    $cert_locality   = $cert['props']['locality']
    $cert_unit       = $cert['props']['unit']
    $cert_bit        = $cert['props']['bit']
    $cert_days       = $cert['props']['days']

    ## create ssl certificate
    exec { 'create-ssl-certificate':
      command  => dos2unix(template('webserver/ssl.erb')),
      unless   => [
        "test -f ${cert_path}/${vhost}.crt",
        "test -f ${pkey_path}/${vhost}.key",
      ],
      path     => '/usr/bin',
      provider => shell,
    }
}
