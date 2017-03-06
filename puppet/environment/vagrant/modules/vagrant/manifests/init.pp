###
### init.pp: ensure 'vagrant-mounted' event fires, when '/vagrant' shared
###          directory, is mounted within the guest virtual machine.
###

class vagrant {
    ## configure service
    include vagrant::service

    ## start service
    include vagrant::start
}