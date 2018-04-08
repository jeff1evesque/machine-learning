###
### install.pp, install sklearn.
###
class sklearn::install {
    contain python

    ## local variables
    $version     = $::sklearn::scikit_learn

    ## install scikit-learn
    package { 'scikit-learn':
        ensure   => $version,
        provider => 'pip',
        require  => Class['python'],
    }
}