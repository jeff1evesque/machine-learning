###
### params.pp: default class parameters.
###
### @members, corresponds to an existing webserver.
###
class reverse_proxy::params {
    $hiera                   = lookup( { 'name' => 'webcompiler', 'default_value' => false } )
    $run                     = true
    $node_version            = 'latest'
    $node_sass_version       = 'latest'

    if $hiera {
        $root_dir            = $hiera['webcompiler']['root_dir']
        $root_puppet         = $hiera['webcompiler']['root_puppet']
        $user                = $hiera['webcompiler']['root_puppet']
        $group               = $hiera['webcompiler']['group']
    }

    else {
        $root_dir            = '/var/machine-learning'
        $root_puppet         = '/etc/puppetlabs'
        $user                = 'root'
        $group               = 'root'
    }
}
