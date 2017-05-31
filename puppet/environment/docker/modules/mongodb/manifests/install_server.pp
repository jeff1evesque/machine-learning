###
### Install mongodb server.
###
class mongodb::install_server {
    package { 'mongodb-org-server':
        ensure  => installed,
    }
}
