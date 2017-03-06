###
### vagrant_mounted.pp: ensure 'vagrant-mounted' event fires, when '/vagrant'
###                     shared directory, is mounted within the guest virtual
###                     machine.
###

## configure service
include vagrant::service

## start service
include vagrant::start