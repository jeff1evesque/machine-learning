FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/scss $ROOT_PROJECT/interface/static/css
COPY src/scss/package.json $ROOT_PROJECT/src
COPY src/scss $ROOT_PROJECT/src/scss

## provision with package.json
WORKDIR $ROOT_PROJECT/src/
RUN npm install

## define entrypoint script
RUN printf '#!/bin/bash\n\n\
npm run build:css\n\
npm run watch:scss\n\
' > $ROOT_PROJECT/src/entrypoint
RUN chmod 710 $ROOT_PROJECT/src/entrypoint

## executed everytime container starts
ENTRYPOINT ["/bin/bash", "-c", "./entrypoint"]
