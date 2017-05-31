###
### init.pp: start webserver, and ensure all client services exist, and
###          properly configured.
###

class webserver {
    ## install mariadb client
    contain mariadb::client
    contain mariadb::bindings

    ## create mongodb users
    contain mongodb::download
    contain mongodb::install_shell
    contain mongodb::create_users

    ## install redis client
    contain package::redis_client

    ## ssl for nginx
    contain webserver::ssl

    ## install webserver
    contain package::gunicorn
    contain webserver::service
}
contain webserver