###
### sklearn_dependencies.pp, install sklearn related packages.
###
class package::sklearn_dependencies {
    include package::python_dev

    ## local variables
    $hiera_dev            = lookup('development')
    $version_python_numpy = $hiera_dev['apt']['python-numpy']
    $version_python_scipy = $hiera_dev['apt']['python-scipy']
    $version_libatlas_dev = $hiera_dev['apt']['libatlas-dev']
    $version_gplus        = $hiera_dev['apt']['gplus']
    $version_python_lib   = $hiera_dev['apt']['python-matplotlib']
    $version_ipython      = $hiera_dev['apt']['ipython']

    $dependencies = [
        "python-numpy=${$version_python_numpy}",
        "python-scipy=${version_python_scipy}",
        "libatlas-dev=${version_libatlas_dev}",
        "g++=${version_gplus}",
        "python-matplotlib=${version_python_lib}",
        "ipython=${version_ipython}"
    ]

    ## install dependencies
    ensure_packages( $dependencies )
}