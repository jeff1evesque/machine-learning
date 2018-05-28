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
npm run prebuild:dos2unix\n\
if [ "$1" == 'test' ]; then\n\
  npm run test:coveralls\n\
else\n\
  npm run build:browserify\n\
  npm run watch:jsx\n\
fi\n\
' > $ROOT_PROJECT/src/jsx/entrypoint
RUN chmod 710 $ROOT_PROJECT/src/jsx/entrypoint

## executed everytime container starts
ENTRYPOINT ["./entrypoint"]
