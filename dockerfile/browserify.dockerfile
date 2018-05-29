FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/jsx $ROOT_PROJECT/interface/static/js $ROOT_PROJECT/src/jsx/dockerfile $ROOT_PROJECT/test/jest
COPY src/jsx test/jest $ROOT_PROJECT/src/jsx/
COPY dockerfile/browserify.dockerfile src/jsx/dockerfile/browserify.dockerfile

## provision with package.json
WORKDIR $ROOT_PROJECT/src/jsx
RUN npm install

## define entrypoint script
RUN printf '#!/bin/bash\n\n\
npm run prebuild:dos2unix\n\
npm run build:browserify\n\
npm run watch:jsx\n\
' > $ROOT_PROJECT/src/jsx/entrypoint
RUN chmod 710 $ROOT_PROJECT/src/jsx/entrypoint

## executed everytime container starts
ENTRYPOINT ["./entrypoint"]
