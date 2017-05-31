###
### Configures mongodb instance.
###

class mongodb {
    contain mongodb::download
    contain mongodb::install_server
    contain mongodb::install_shell
    contain mongodb::run
}
contain mongodb