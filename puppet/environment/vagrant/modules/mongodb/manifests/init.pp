###
### Configures mongodb instance.
###

class mongodb {
    contain mongodb::install
    contain mongodb::run
    contain mongodb::create_users
}