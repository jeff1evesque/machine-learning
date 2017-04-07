###
### sklearn.pp, clone github codebase.
###
class package::sklearn {
    require git

    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    $hiera_dev     = lookup('development')
    $version       = $hiera_dev['github']['custom']['sklearn']

    ## download sklearn
    vcsrepo { "${root_dir}/build/scikit-learn":
        ensure   => present,
        provider => git,
        source   => 'https://github.com/scikit-learn/scikit-learn',
        revision => $version,
    }
}