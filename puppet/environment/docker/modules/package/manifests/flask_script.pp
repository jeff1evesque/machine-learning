###
### flask_script.pp, install package.
###
class package::flask_script {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['flask-script']

    package { 'Flask-Script':
        ensure   => $version,
        provider => 'pip',
    }
}