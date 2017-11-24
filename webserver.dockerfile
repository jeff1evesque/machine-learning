FROM ml-default

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## create source containers
RUN mkdir -p /var/machine-learning/src/jsx
RUN mkdir -p /var/machine-learning/src/js
RUN mkdir -p /var/machine-learning/src/scss
RUN mkdir -p /var/machine-learning/src/img

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/webserver/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test

## executed everytime container starts
WORKDIR /var/machine-learning
ENTRYPOINT ["python", "app.py"]