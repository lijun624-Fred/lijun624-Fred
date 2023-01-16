# resource "azurerm_resource_group" "demo3_rg" {
#   name                = var.databricks_var["rg_name"]
#   location            = var.databricks_var["rg_location"]
# }

# resource "azurerm_databricks_workspace" "demo3_databricks" {
#   name                = var.databricks_var["dbs_name"]
#   resource_group_name = azurerm_resource_group.demo3_rg.name
#   location            = azurerm_resource_group.demo3_rg.location
#   sku                 = var.databricks_var["dbs_sku"]

#   tags = {
#     Environment       = var.databricks_var["dbs_tags"]
#   }
# }