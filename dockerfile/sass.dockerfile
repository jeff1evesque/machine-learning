FROM node:9
USER node

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/scss $ROOT_PROJECT/interface/static/css
COPY src/scss $ROOT_PROJECT/src/scss

##
## change npm-global directory
##
## Note: prevent an infinite node-gyp loop, regarding permission error:
##
##     - https://github.com/nodejs/node-gyp/issues/1236#issuecomment-328872985
##
RUN mkdir /home/node/.npm-global; \
    chown -R node:node /home/node/.npm-global
ENV PATH=/home/node/.npm-global/bin:$PATH
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

## install node-sass
RUN npm install -g node-sass

## executed everytime container starts
CMD node-sass --watch ${ROOT_PROJECT}/src/scss --output ${ROOT_PROJECT}/interface/static/css
