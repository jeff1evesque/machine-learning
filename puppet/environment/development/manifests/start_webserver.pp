## create log directory
include system::log_directory

## install webserver
include webserver::service

## detect os family: create startup script, start flask server
include webserver::start