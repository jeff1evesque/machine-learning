###
### Configures mongodb databases.
###

class mongodb_cluster::configure_databases {
    ## local variables
    $hiera_database = lookup('database')
    $hiera_mongodb  = $hiera_database['mongodb_cluster']
    $hiera_user     = $hiera_mongodb['user']
    $admin_user     = $hiera_user['admin']['name']
    $admin_password = $hiera_user['admin']['password']

    mongodb::db { 'svm_dataset':
        user          => $admin_user,
        password_hash => $admin_password,
    }

    mongodb::db { 'svr_dataset':
        user          => $admin_user,
        password_hash => $admin_password,
    }
}
