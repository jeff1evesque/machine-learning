###
### init.pp: install, configure, and run initial compile against source files.
###

class compiler {
    ## ensure log directory, package dependencies
    require system::log_directory

    ## configure webcompilers
    require system::webcompiler_directory
    contain compiler::webcompilers

    ## start compiler(s)
    contain compiler::start_sass
    contain compiler::start_uglifyjs
    contain compiler::start_browserify

    ## initial compile
    contain compiler::initial_compile
}
contain compiler