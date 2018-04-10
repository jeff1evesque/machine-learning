###
### params.pp: default class parameters.
###
class mariadb::params {
    $hiera                    = lookup( { 'name' => 'database', 'default_value' => false } )
    $root_puppet              = '/etc/puppetlabs'
    $pyyaml_version           = '*'

    if $hiera {
        $root_dir             = $hiera['root_dir']
        $db_host              = $hiera['mariadb']['host']
        $db                   = $hiera['mariadb']['name']
        $db_user              = $hiera['mariadb']['username']
        $db_password          = $hiera['mariadb']['password']
        $provisioner          = $hiera['mariadb']['provisioner']
        $provisioner_password = $hiera['mariadb']['provisioner_password']
        $tester               = $hiera['mariadb']['tester']
        $tester_password      = $hiera['mariadb']['tester_password']
        $root_password        = $hiera['mariadb']['root_password']
        $bind_address         = $hiera['mariadb']['bind_address']
        $allow_host           = $hiera['mariadb']['allow_host']
    }

    else {
        $root_dir             = '/var/machine-learning'
        $db_host              = 'mariadb'
        $db                   = 'default'
        $db_user              = 'authenticated'
        $db_password          = 'password'
        $provisioner          = 'provisioner'
        $provisioner_password = 'password'
        $tester               = 'tester'
        $tester_password      = 'password'
        $root_password        = 'password'
        $bind_address         = '0.0.0.0'
        $allow_host           = '%'
    }
}
