### setup_database.pp: install client, and initialize database tables.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## install mariadb
include database::server

## install mariadb client
include database::client

## install mariad bindings
include database::bindings

## create database tables
include database::database