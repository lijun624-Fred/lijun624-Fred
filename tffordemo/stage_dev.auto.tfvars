databricks_var = {
    rg_name        = "demo3"
    rg_location    = "China North 3"
    dbs_name       = "demo3_databricks"
    dbs_sku        = "standard"
    dbs_tags       = "demo3"
}

app_service_var = {
    rg_name        = "DefaultResourceGroup-CNE2-chinanorth3"
    rg_location    = "China North 3"
    app_name       = "demo4"
    plan_name      = "ASP-DefaultResourceGroupCNE2chinano-81bf"
    plan_tier      = "Basic"
    plan_size      = "Small"
    scm_type       = "ExternalGit"
    dbhost         = "demo4-sql.postgres.database.chinacloudapi.cn"
    dbname         = "postgres"
    dbuser         = "admindemo4"
    dbpass         = "Demo4sql"
}