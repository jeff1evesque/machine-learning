FROM ubuntu:14.04

## install git, and wget
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install wget -y

## install openssh
RUN apt-get install openssh-client

## private github deploy ssh-key (readonly)
RUN mkdir ~/.ssh && chmod 700 ~/.ssh
RUN eval $(ssh-agent -s)
RUN echo $'\
-----BEGIN RSA PRIVATE KEY----- Proc-Type: 4,ENCRYPTED DEK-Info:\n\ 
AES-128-CBC,1CAD9620987F3B7D76E0ADB05740C448\n\
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\n\
-----END RSA PRIVATE KEY-----\n'\
>> ~/.ssh/id_rsa

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
RUN dpkg -i puppetlabs-release-trusty.deb
RUN apt-get update -y

## install r10k
RUN apt-get install rubygems-integration -y
RUN gem install r10k

## clone repository: allow puppet manifests to run (below)
RUN git clone https://jeff1evesque@github.com/jeff1evesque/machine-learning.git /var/machine-learning

## install puppet modules using puppetfile with r10k
RUN PUPPETFILE=/var/machine-learning/puppet/Puppetfile PUPPETFILE_DIR=/var/machine-learning/puppet/modules/ r10k puppetfile install

## provision with puppet
RUN for x in $(find . -name '/var/machine-learning/puppet/manifests/*.pp'); do puppet apply $x; done;
