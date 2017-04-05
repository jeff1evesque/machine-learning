###
### Configures mongodb instance.
###

class mongodb {
    contain mongodb::install
    contain mongodb::run
}