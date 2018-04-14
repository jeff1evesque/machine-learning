FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## source + asset directory
COPY src/jsx $ROOT_PROJECT/jsx
RUN mkdir -p $ROOT_PROJECT/interface/static/js

## provision with package.json
WORKDIR src
RUN npm install

## executed everytime container starts
CMD ["npm", "run-script", "watch:jsx"]
