###
### scrypt.pp, install package.
###
class package::scrypt {
    require python
    import package::python_dev

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['scrypt']

    package { 'scrypt':
        ensure   => $version,
        provider => 'pip',
        require  => Class['package::python_dev'],
    }
}