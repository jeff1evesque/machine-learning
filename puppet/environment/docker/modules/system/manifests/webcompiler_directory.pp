###
### webcompiler_directory.pp, create webcompiler subdirectories.
###
class system::webcompiler_directory {
    ## local variables
    $hiera_general = lookup('general')
    $root_dir      = $hiera_general['root']

    $directories = {
        browserify => {
            src       => 'jsx',
            asset     => 'js',
            asset_dir => true,
            src_dir   => true,
        },
        imagemin   => {
            src   => 'img',
            asset => 'img',
            asset_dir => true,
            src_dir   => true,
        },
        sass       => {
            src       => 'scss',
            asset     => 'css',
            asset_dir => true,
            src_dir   => true,
        },
        uglifyjs   => {
            src       => 'js',
            asset     => 'js',
            asset_dir => false,
            src_dir   => false,
        }
    }

    $directories.each |String $directory, Hash $compiler| {
        ## create asset directories (if not exist)
        if ($compiler['asset_dir']) {
            file { "${root_dir}/interface/static/${compiler['asset']}/":
                ensure => 'directory',
            }
        }

        ## create src directories (if not exist)
        if ($compiler['src_dir']) {
            file { "${root_dir}/src/${compiler['src']}/":
                ensure => 'directory',
            }
        }
    }
}