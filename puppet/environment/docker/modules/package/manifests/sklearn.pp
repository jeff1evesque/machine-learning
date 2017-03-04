### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::sklearn {
    require git

    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    $hiera_dev     = lookup('development')
    $version       = $hiera_dev['github']['sklearn']

    ## download sklearn
    vcsrepo { "${root_dir}/build/scikit-learn":
        ensure   => present,
        provider => git,
        source   => 'https://github.com/scikit-learn/scikit-learn',
        revision => $version,
    }
}