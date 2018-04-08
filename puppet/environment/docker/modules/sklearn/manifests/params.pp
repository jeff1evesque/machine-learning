###
### params.pp: default class parameters.
###
class sklearn::params {
    $hiera             = lookup( { 'name' => 'sklearn', 'default_value' => false } )
    $python_numpy      = 'latest'
    $python_scipy      = 'latest'
    $libatlas_dev      = 'latest'
    $gplus             = 'latest'
    $ipython           = 'latest'
    $python_dev        = 'latest'
    $python_matplotlib = 'latest'

    if $hiera {
        $root_dir      = $hiera['root_dir']
    }

    else {
        $root_dir      = '/var/machine-learning'
    }
}
