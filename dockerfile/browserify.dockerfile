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

##
## dos2unix + browserify
##
## Note: to persist the container:
##
##     docker run --hostname browserify --name browserify -d jeff1evesque/ml-browserify:0.7 tail -f /dev/null
##
ENTRYPOINT inotifywait $ROOT_PROJECT/src/jsx/ -m -r -e close_write -e move | \
    browserify $ROOT_PROJECT/src/jsx/content.jsx \
    -t [ babelify --presets env,stage-2,react ] \
    -o $ROOT_PROJECT/src/js/content.js
CMD tail -f /dev/null
