###
### Install mongodb server.
###
class mongodb::install_server {
    include mongodb::download

    package { 'mongodb-org-server':
        ensure  => installed,
        require => [
            Exec['apt-key-puppetlabs'],
            File['mongodb-list-file'],
            Exec['apt-get-update'],
        ],
    }
}
