FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/jsx $ROOT_PROJECT/interface/static/js
COPY src/jsx/package.json $ROOT_PROJECT/src
COPY src/jsx $ROOT_PROJECT/src/jsx

## provision with package.json
WORKDIR $ROOT_PROJECT/src
RUN apt-get update && apt-get install -y inotify-tools dos2unix
RUN npm install -g browserify
RUN npm install

## dos2unix + browserify
CMD inotifywait $ROOT_PROJECT/src/jsx/ -m -r -e close_write -e move | \
    find . -type f -print0 | xargs -0 dos2unix \
    browserify $ROOT_PROJECT/src/jsx/content.jsx \
    -t [ babelify --presets env,stage-2,react ] \
    -o $ROOT_PROJECT/src/js/content.js
