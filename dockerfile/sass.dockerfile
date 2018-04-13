FROM node:9
USER node

## local variables
ENV ROOT_PROJECT /var/machine-learning

## create directories
COPY src/scss $ROOT_PROJECT/src/scss
COPY interface/static/css $ROOT_PROJECTinterface/static/css

## change npm-global directory
RUN mkdir /home/node/.npm-global; \
    mkdir -p /home/node/app; \
    chown -R node:node $ROOT_PROJECT/src/scss; \
    chown -R node:node $ROOT_PROJECTinterface/static/css; \
    chown -R node:node /home/node/.npm-global
ENV PATH=/home/node/.npm-global/bin:$PATH
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

## install node-sass
RUN npm install -g node-sass

## executed everytime container starts
CMD [\
    "/bin/sh",\
    "-c",\
    "node-sass",\
    "-w",\
    "$ROOT_PROJECT/src/scss",\
    "-o",\
    "$ROOT_PROJECT/interface/static/css",\
    "&"\
]