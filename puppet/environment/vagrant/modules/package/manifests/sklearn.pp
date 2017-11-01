###
### sklearn.pp, install scikit-learn.
###
class package::sklearn {
    require python

    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    $hiera_dev     = lookup('development')
    $version       = $hiera_dev['pip']['general']['scikit-learn']

    ## install scikit-learn
    package { 'scikit-learn':
        ensure   => $version,
        provider => 'pip',
        require  => Class['python'],
    }
}