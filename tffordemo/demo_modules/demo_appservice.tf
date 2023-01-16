resource "azurerm_app_service_plan" "demo4" {
  name                = var.app_service_var["plan_name"]
  location            = data.azurerm_resource_group.cn3.location
  resource_group_name = data.azurerm_resource_group.cn3.name
  kind                = var.app_service_var["kind"]
  reserved            = var.app_service_var["reserved"] 

  sku {
    tier              = var.app_service_var["plan_tier"]
    size              = var.app_service_var["plan_size"]
  }
  tags = {
    scope             = var.app_service_var["pip3_tag"]
  }
}

resource "azurerm_app_service" "demo4" {
  name                = var.app_service_var["app_name"]
  location            = data.azurerm_resource_group.cn3.location
  resource_group_name = data.azurerm_resource_group.cn3.name
  app_service_plan_id = azurerm_app_service_plan.demo4.id
  https_only          = var.app_service_var["https"] 

  site_config {
    scm_type          = var.app_service_var["scm_type"]
    use_32_bit_worker_process = var.app_service_var["bit_worker"]
    default_documents = ["Default.html","index.html"]
  }

  app_settings = {
    DBHOST            = var.app_service_var["dbhost"]
    DBNAME            = var.app_service_var["dbname"]
    DBPASS            = var.app_service_var["dbpass"]
    DBUSER            = var.app_service_var["dbuser"]
  }
  tags = {
    scope             = var.app_service_var["pip3_tag"]
  }
}

resource "azurerm_app_service_virtual_network_swift_connection" "demo4" {
  app_service_id      = azurerm_app_service.demo4.id
  subnet_id           = data.azurerm_subnet.demo4_subnet.id
}