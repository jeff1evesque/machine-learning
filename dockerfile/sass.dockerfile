FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/scss $ROOT_PROJECT/interface/static/css
COPY src/scss/package.json $ROOT_PROJECT/src
COPY src/scss $ROOT_PROJECT/src/scss

## provision with package.json
WORKDIR $ROOT_PROJECT/src
RUN npm install

## executed everytime container starts
CMD ["npm", "run", "watch:scss"]
