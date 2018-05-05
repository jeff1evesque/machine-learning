###
### install.pp, install jest.
###
class jest::install {
    ## local variables
    $version   = $::jest::version

    ## install jess
    package { 'jest-cli':
        ensure   => $version,
        provider => 'npm',
    }
}