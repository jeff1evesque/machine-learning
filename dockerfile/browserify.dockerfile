FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
COPY src/package.json src/jsx $ROOT_PROJECT/
RUN mkdir -p $ROOT_PROJECT/interface/static/js

## provision with package.json
WORKDIR $ROOT_PROJECT/src
RUN npm install

## executed everytime container starts
CMD ["npm", "run-script", "watch:jsx"]
