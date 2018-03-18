###
### init.pp: configure, and start nginx.
###
class nginx {
    ## ensure log directory
    require system::log_directory

    ## configure nginx
    contain nginx::ssl
    contain nginx::service
}
contain nginx
