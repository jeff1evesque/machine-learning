###
### init.pp: start webserver.
###

class webserver {
    ## ensure log directory
    require system::log_directory

    ## install webserver
    include webserver::service

    ## start webservers
    include package::gunicorn
    include webserver::start
}