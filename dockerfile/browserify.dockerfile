FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
RUN mkdir -p $ROOT_PROJECT/src/jsx $ROOT_PROJECT/interface/static/js
COPY src/package.json src/jsx $ROOT_PROJECT/src

## provision with package.json
WORKDIR $ROOT_PROJECT/src
RUN npm install

## executed everytime container starts
CMD ["npm", "run", "watch:jsx"]
