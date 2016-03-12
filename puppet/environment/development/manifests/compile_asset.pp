### compile_asset.pp: install, configure, and run initial compile against
###                   source files.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## configure webcompilers
include compiler::webcompilers

## start webcompilers
include compiler::start_sass
include compiler::start_uglifyjs
include compiler::start_browserify
include compiler::start_imagemin

## initial compiler
include compiler::initial_compile