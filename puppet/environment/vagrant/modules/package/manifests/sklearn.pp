###
### sklearn.pp, install scikit-learn.
###
class package::sklearn {
    require python

    ## local variables
    $hiera_dev     = lookup('development')
    $version       = $hiera_dev['pip']['custom']['scikit-learn']

    ## install scikit-learn
    package { 'scikit-learn':
        ensure   => $version,
        provider => 'pip',
        require  => Class['python'],
    }
}