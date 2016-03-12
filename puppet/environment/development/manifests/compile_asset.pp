## configure webcompilers
include compiler::webcompilers

## start webcompilers
include compiler::start_sass
include compiler::start_uglifyjs
include compiler::start_browserify
include compiler::start_imagemin

## initial compiler
include compiler::initial_compile