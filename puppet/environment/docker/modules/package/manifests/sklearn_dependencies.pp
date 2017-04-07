###
### sklearn_dependencies.pp, install sklearn related packages.
###
class package::sklearn_dependencies {
    contain package::python_dev

    ## local variables
    $hiera_dev            = lookup('development')
    $version_python_numpy = $hiera_dev['apt']['custom']['python-numpy']
    $version_python_scipy = $hiera_dev['apt']['custom']['python-scipy']
    $version_libatlas_dev = $hiera_dev['apt']['custom']['libatlas-dev']
    $version_gplus        = $hiera_dev['apt']['custom']['gplus']
    $version_python_lib   = $hiera_dev['apt']['custom']['python-matplotlib']
    $version_ipython      = $hiera_dev['apt']['custom']['ipython']

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