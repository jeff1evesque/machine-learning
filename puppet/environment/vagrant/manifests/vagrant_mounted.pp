### vagrant_mounted.pp: ensure 'vagrant-mounted' event fires, when '/vagrant'
###                     shared directory, is mounted within the guest virtual
###                     machine.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## configure service
include vagrant::service

## start service
include vagrant::start