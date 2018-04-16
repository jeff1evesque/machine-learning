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

## executed everytime container starts
ENTRYPOINT ["npm", "run", "watch:jsx"]
