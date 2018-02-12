FROM ml-default

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## copy files into container
COPY src /var/machine-learning/src
COPY test /var/machine-learning/test
COPY hiera /var/machine-learning/hiera
COPY interface /var/machine-learning/interface

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/compiler/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test

## executed everytime container starts
WORKDIR /var/machine-learning/test/jest
ENTRYPOINT ["jest", "--config", "jest.config.js"]