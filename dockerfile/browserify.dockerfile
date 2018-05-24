FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/jsx $ROOT_PROJECT/interface/static/js
COPY src/jsx test/jest/setup.js test/jest/jest.config.js $ROOT_PROJECT/src/jsx/
COPY test/jest/__tests__ $ROOT_PROJECT/src/jsx/__tests__

## provision with package.json
WORKDIR $ROOT_PROJECT/src/jsx
RUN npm install

## define entrypoint script
RUN printf '#!/bin/bash\n\n\
args="$1"\n\n\
npm run prebuild:dos2unix\n\
npm run build:browserify\n\
if [ -z "$args" ]; then npm run watch:jsx; fi\n\
' > $ROOT_PROJECT/src/jsx/entrypoint
RUN chmod 710 $ROOT_PROJECT/src/jsx/entrypoint

## executed everytime container starts
ENTRYPOINT ["/bin/bash", "-c", "./entrypoint"]
