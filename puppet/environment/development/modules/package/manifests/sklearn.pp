### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::sklearn {
    require git

    ## local variables
    $root_dir = hiera('general')['root']

    ## download sklearn
    vcsrepo { "${root_dir}/build/scikit-learn":
        ensure   => present,
        provider => git,
        source   => 'https://github.com/scikit-learn/scikit-learn',
        revision => '0.16.1',
    }
}