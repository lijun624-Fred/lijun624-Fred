module "azuredemo" {
  source                   = "./demo_modules/"
  databricks_var           = var.databricks_var
  app_service_var          = var.app_service_var
  postgre_sql_var          = var.postgre_sql_var
}