###
### init.pp: install, configure, and run initial compile against
###                   source files.
###

class compiler {
    ## ensure log directory, package dependencies
    class dependencies {
        require system::log_directory
        contain package::webcompilers
    }

    ## configure webcompilers
    class configure {
        ## set dependency
        require dependencies

        ## configure webcompilers	
        require system::webcompiler_directory
        contain compiler::webcompilers
    }

    ## start webcompilers
    class start {
        ## set dependency
        require dependencies
        require configure

        ## start compiler(s)
        contain compiler::start_sass
        contain compiler::start_uglifyjs
        contain compiler::start_browserify
        contain compiler::start_imagemin
    }

    ## initial compile
    class initiate {
        ## set dependency
        require dependencies
        require configure
        require start

        ## initial compile
        contain compiler::initial_compile
    }

    ## initiate
    include initiate
}