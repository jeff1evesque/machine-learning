###
### install.pp, install sklearn.
###
class sklearn::install {
    include python

    ## local variables
    $root_dir          = $::sklearn::root_dir
    $scikit_learn      = $::sklearn::scikit_learn
    $python_numpy      = $::sklearn::python_numpy
    $python_scipy      = $::sklearn::python_scipy
    $libatlas_dev      = $::sklearn::libatlas_dev
    $gplus             = $::sklearn::gplus
    $python_matplotlib = $::sklearn::python_matplotlib
    $ipython           = $::sklearn::ipython
    $python_dev        = $::sklearn::python_dev
    $apt_packages      = [
        "g++=${gplus}",
        "python-dev=${python_dev}",
        "python-numpy=${python_numpy}",
        "python-scipy=${python_scipy}",
        "libatlas-dev=${libatlas_dev}",
        "ipython=${ipython}",
        "python-matplotlib=${python_matplotlib}",
    ]

    ## install scikit-learn dependencies
    package { $apt_packages:
        ensure   => 'installed',
    }

    ## install scikit-learn
    if ($scikit_learn and $scikit_learn != '*') {
        package { "scikit_learn==${scikit_learn}":
            ensure   => 'installed',
            provider => 'pip',
            require  => Class['python'],
        }
    }
    else {
        package { 'scikit_learn':
            ensure   => 'installed',
            provider => 'pip',
            require  => Class['python'],
        }
    }
}