FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## create directories
COPY src/scss $ROOT_PROJECT/src/scss
COPY interface/static/css $ROOT_PROJECTinterface/static/css

## provision with puppet
RUN npm install node-sass

## executed everytime container starts
CMD [\
    "node-sass",\
    "-w",\
    "$ROOT_PROJECT/src/scss",\
    "-o",\
    "$ROOT_PROJECT/interface/static/css"\
]