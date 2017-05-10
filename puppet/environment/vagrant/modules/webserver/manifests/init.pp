###
### init.pp: start webserver.
###

class webserver {
    ## ensure log directory
    require system::log_directory

    ## ssl for nginx
    contain webserver::ssl

    ## install webserver
    contain webserver::service

    ## start webservers
    contain package::pyyaml
    contain package::gunicorn
    contain webserver::start
}