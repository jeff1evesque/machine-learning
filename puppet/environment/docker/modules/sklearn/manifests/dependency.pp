###
### dependency.pp, install sklearn dependencies.
###
class sklearn::dependency {
    ## local variables
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

    ## build directory
    file { "${root_dir}/build/":
        ensure    => 'directory',
    }
}