FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/jsx $ROOT_PROJECT/interface/static/js
COPY src/jsx/package.json $ROOT_PROJECT/src
COPY src/jsx $ROOT_PROJECT/src/jsx

## provision with package.json
WORKDIR $ROOT_PROJECT/src
RUN npm install

## define entrypoint script
RUN printf "#!/bin/bash\n\n\
npm run watch:jsx && npm run postbuild:touch\n\
" > $ROOT_PROJECT/src/entrypoint
RUN chmod 710 $ROOT_PROJECT/src/entrypoint

## executed everytime container starts
ENTRYPOINT ["/bin/bash", "-c", "./entrypoint"]
