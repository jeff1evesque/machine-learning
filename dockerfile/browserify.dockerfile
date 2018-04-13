FROM node:9

## local variables
ENV ROOT_PROJECT /var/machine-learning

## copy files into container
COPY src/jsx $ROOT_PROJECT/jsx
COPY interface/static/js $ROOT_PROJECT/interface/static/js

## provision with puppet
WORKDIR src
RUN npm install

## executed everytime container starts
CMD ["npm", "run-script", "watch:jsx"]
