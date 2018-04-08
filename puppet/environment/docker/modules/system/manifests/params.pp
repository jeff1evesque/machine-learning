###
### params.pp: default class parameters.
###
class mariadb::params {
    $hiera        = lookup( { 'name' => 'system', 'default_value' => false } )

    if $hiera {
        $regions  = $hiera['timezone']['region']
        $locality = $hiera['timezone']['locality']
    }

    else {
        $regions  = 'America'
        $locality = 'New_York
    }
}
