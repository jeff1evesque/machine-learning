###
### Configures mongodb databases.
###

class mongodb_cluster::databases {
    ## local variables
    $hiera_mongodb  = lookup('mongodb_cluster')
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
