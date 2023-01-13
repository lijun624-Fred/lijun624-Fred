resource "azurerm_resource_group" "cn3" {
  name                = var.app_service_var["rg_name"]
  location            = var.app_service_var["rg_location"]
}

resource "azurerm_app_service_plan" "demo4" {
  name                = var.app_service_var["plan_name"]
  location            = azurerm_resource_group.cn3.location
  resource_group_name = azurerm_resource_group.cn3.name

  sku {
    tier              = var.app_service_var["plan_tier"]
    size              = var.app_service_var["plan_size"]
  }
}

resource "azurerm_app_service" "demo4" {
  name                = var.app_service_var["app_name"]
  location            = azurerm_resource_group.cn3.location
  resource_group_name = azurerm_resource_group.cn3.name
  app_service_plan_id = azurerm_app_service_plan.demo4.id

  site_config {
    scm_type          = var.app_service_var["scm_type"]
  }

  app_settings = {
    DBHOST            = var.app_service_var["dbhost"]
  }
}

resource "azurerm_app_service_virtual_network_swift_connection" "demo4" {
  app_service_id      = azurerm_app_service.demo4.id
  subnet_id           = data.azurerm_subnet.demo4_subnet.id
}