###
### init.pp: start webserver, and ensure all client services exist, and
###          properly configured.
###

class webserver {
    ## install mariadb
    include database::client
    include database::bindings

    ## install redis client
    include package::redis_client

    ## install webserver
    include package::gunicorn
    include webserver::service
}