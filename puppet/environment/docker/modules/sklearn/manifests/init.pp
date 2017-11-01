###
### init.pp: install sklearn, with all necessary dependencies.
###

class sklearn {
    ## create '/vagrant/build/' directory
    contain system::build_directory

    ## install sklearn dependencies
    contain package::sklearn_dependencies

    ## install scikit-learn
    contain package::sklearn
}
contain sklearn