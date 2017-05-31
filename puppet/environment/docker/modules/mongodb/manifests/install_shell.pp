###
### Install mongodb shell.
###
class mongodb::install_shell {
    include mongodb::download

    package { 'mongodb-org-shell':
        ensure  => installed,
        require => [
            Exec['apt-key-puppetlabs'],
            File['mongodb-list-file'],
            Exec['apt-get-update'],
        ],
    }
}
