FROM ml-base

## local variables
ENV ENVIRONMENT docker
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PROJECT /var/machine-learning
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib

## copy files into container
COPY log $ROOT_PROJECT/log
COPY interface $ROOT_PROJECT/interface
COPY hiera $ROOT_PROJECT/hiera
COPY brain $ROOT_PROJECT/brain
COPY test $ROOT_PROJECT/test
COPY app.py $ROOT_PROJECT/app.py
COPY factory.py $ROOT_PROJECT/factory.py
COPY __init__.py $ROOT_PROJECT/__init__.py
COPY puppet/environment/$ENVIRONMENT/modules/sklearn $ROOT_PUPPET/code/modules/sklearn
COPY puppet/environment/$ENVIRONMENT/modules/webserver $ROOT_PUPPET/code/modules/webserver
ARG PORT

## provision with puppet
RUN $PUPPET apply $MODULES/sklearn/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

##
## provision with puppet: either build a web, or api webserver image.
##
##     docker build --build-arg PORT=6001 -f webserver.dockerfile -t ml-webserver-api .
##     docker build --build-arg PORT=5001 -f webserver.dockerfile -t ml-webserver-web .
##
##     docker run --hostname webserver-api --name webserver-api -d ml-webserver-api
##     docker run --hostname webserver-web --name webserver-web -d ml-webserver-web
##
RUN $PUPPET apply -e "class { reverse_proxy: \
    port => '$PORT', \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## executed everytime container starts
WORKDIR $ROOT_PROJECT
ENTRYPOINT ["python", "app.py"]