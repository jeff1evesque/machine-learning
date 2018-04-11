FROM jeff1evesque/ml-sklearn:0.7

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib
ARG PORT
ARG TYPE

## ensure directory
RUN mkdir -p $ROOT_PROJECT/interface $ROOT_PUPPET/brain $ROOT_PUPPET/test

## copy files into container
COPY log interface hiera brain test app.py factory.py __init__.py $ROOT_PROJECT/
COPY puppet/environment/$ENVIRONMENT/modules/webserver $ROOT_PUPPET/code/modules/webserver

##
## provision with puppet: either build a web, or api webserver image.
##
##     docker build --build-arg PORT=6001 --build-arg TYPE=api -f webserver.dockerfile -t ml-webserver-api .
##     docker build --build-arg PORT=5001 --build-arg TYPE=web -f webserver.dockerfile -t ml-webserver-web .
##
##     docker run --hostname webserver-api --name webserver-api -d ml-webserver-api
##     docker run --hostname webserver-web --name webserver-web -d ml-webserver-web
##
RUN $PUPPET apply -e "class { webserver: \
    gunicorn_type => '$TYPE', \
    gunicorn_port => '$PORT', \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
WORKDIR $ROOT_PROJECT
ENTRYPOINT ["python", "app.py"]