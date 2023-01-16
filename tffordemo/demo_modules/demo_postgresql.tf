resource "azurerm_private_dns_zone" "demo4" {
  name                  = var.postgre_sql_var["private_dns_name"]
  resource_group_name   = data.azurerm_resource_group.cn3.name
  tags = {
    scope               = var.app_service_var["pip3_tag"]
  }  
}

resource "azurerm_private_dns_zone_virtual_network_link" "demo4" {
  name                  = "rxdzlxxhjsp32"
  private_dns_zone_name = var.postgre_sql_var["private_dns_name"]
  virtual_network_id    = data.azurerm_virtual_network.pip3_net.id
  resource_group_name   = data.azurerm_resource_group.cn3.name
  tags = {
    scope               = var.app_service_var["pip3_tag"]
  }  
}

resource "azurerm_postgresql_flexible_server" "demo4" {
  name                   = "demo4-sql"
  resource_group_name    = data.azurerm_resource_group.cn3.name
  location               = data.azurerm_resource_group.cn3.location
  version                = var.postgre_sql_var["sql_version"]
  delegated_subnet_id    = data.azurerm_subnet.db_subnet.id
  private_dns_zone_id    = azurerm_private_dns_zone.demo4.id
  administrator_login    = var.app_service_var["dbuser"]
  administrator_password = var.app_service_var["dbpass"]
  zone                   = var.postgre_sql_var["zone"]
  storage_mb             = var.postgre_sql_var["storage_mb"]
  sku_name               = var.postgre_sql_var["sku_name"]
  depends_on             = [azurerm_private_dns_zone_virtual_network_link.demo4]
  tags = {
    scope                = var.app_service_var["pip3_tag"]
  }
}