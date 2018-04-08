###
### params.pp: default class parameters.
###
class browserify::params {
    $hiera              = lookup( { 'name' => 'webcompiler', 'default_value' => false } )
    $run                = true
    $node_version       = 'latest'
    $browserify_version = 'latest'
    $babel_core_version = 'latest'
    $babelify_version   = 'latest'

    if $hiera {
        $root_dir       = $hiera['webcompiler']['root_dir']
        $root_puppet    = $hiera['webcompiler']['root_puppet']
        $user           = $hiera['webcompiler']['root_puppet']
        $group          = $hiera['webcompiler']['group']
    }

    else {
        $root_dir       = '/var/machine-learning'
        $root_puppet    = '/etc/puppetlabs'
        $user           = 'root'
        $group          = 'root'
    }
}
