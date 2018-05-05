###
### params.pp: default class parameters.
###
class sklearn::params {
    $hiera             = lookup( { 'name' => 'sklearn', 'default_value' => false } )
    $scikit_learn      = '*'
    $python_numpy      = '*'
    $python_scipy      = '*'
    $libatlas_dev      = '*'
    $gplus             = '*'
    $ipython           = '*'
    $python_dev        = '*'
    $python_matplotlib = '*'

    if $hiera {
        $root_dir      = $hiera['root_dir']
    }

    else {
        $root_dir      = '/var/machine-learning'
    }
}
