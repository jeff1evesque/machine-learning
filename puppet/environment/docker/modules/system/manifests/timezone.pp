###
### timezone.pp, set system timezone.
###
class system::timezone {
    ## local variables
    $region      = $::system::region
    $locality    = $::system::locality

    class { 'timezone':
        region   => $region,
        locality => $locality,
    }
}