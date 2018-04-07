###
### params.pp: default class parameters.
###
class mariadb::params {
    $hiera                = lookup( { 'name' => 'database', 'default_value' => false } )
    $run                  = true
    $root_puppet          = '/etc/puppetlabs'
    $pyyaml_version       = 'latest'

    if $hiera {
        $db_host          = $hiera['mariadb']['host']
        $db               = $hiera['mariadb']['name']
        $db_user          = $hiera['mariadb']['username']
        $db_pass          = $hiera['mariadb']['password']
        $provisioner      = $hiera['mariadb']['provisioner']
        $provisioner_pass = $hiera['mariadb']['provisioner_password']
        $tester           = $hiera['mariadb']['tester']
        $tester_pass      = $hiera['mariadb']['tester_password']
        $root_pass        = $hiera['mariadb']['root_password']
        $bind_address     = $hiera['mariadb']['bind_address']
    }

    else {
        $db_host          = 'mariadb'
        $db               = 'default'
        $db_user          = 'authenticated'
        $db_pass          = 'password'
        $provisioner      = 'provisioner'
        $provisioner_pass = 'password'
        $tester           = 'tester'
        $tester_pass      = 'password'
        $root_pass        = 'password'
        $bind_address     = '0.0.0.0'
    }
}
