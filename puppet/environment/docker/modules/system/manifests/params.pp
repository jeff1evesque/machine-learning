###
### params.pp: default class parameters.
###
class mariadb::params {
    $hiera          = lookup( { 'name' => 'system', 'default_value' => false } )
    $nodejs_version = 'latest'

    if $hiera {
        $region     = $hiera['timezone']['region']
        $locality   = $hiera['timezone']['locality']
        $packages   = $hiera['packages']
    }

    else {
        $region     = 'America'
        $locality   = 'New_York'
        $packages   = ''
    }
}
