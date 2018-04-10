###
### install.pp, install sklearn.
###
class sklearn::install {
    contain python

    ## local variables
    $scikit_learn      = $::sklearn::scikit_learn
    $python_numpy      = $::sklearn::python_numpy
    $python_scipy      = $::sklearn::python_scipy
    $libatlas_dev      = $::sklearn::libatlas_dev
    $gplus             = $::sklearn::gplus
    $python_matplotlib = $::sklearn::python_matplotlib
    $ipython           = $::sklearn::ipython
    $root_dir          = $::sklearn::root_dir
    $python_dev        = $::sklearn::python_dev
    $dependencies      = [
        "python-numpy=${python_numpy}",
        "python-scipy=${python_scipy}",
        "libatlas-dev=${libatlas_dev}",
        "g++=${gplus}",
        "python-matplotlib=${python_lib}",
        "ipython=${ipython}",
        "python-dev=${python_dev}"
    ]

    ## install dependencies
    ensure_packages( $dependencies )

    ## install scikit-learn
    package { 'scikit-learn':
        ensure   => $scikit_learn,
        provider => 'pip',
        require  => Class['python'],
    }
}