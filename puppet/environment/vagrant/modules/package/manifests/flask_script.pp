### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::flask_script {
    require python

    package { 'Flask-Script':
        ensure   => '2.0.5',
        provider => 'pip',
    }
}