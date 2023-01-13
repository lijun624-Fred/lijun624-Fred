data "azurerm_virtual_network" "pip3_net" {
  name                 = "pip3-internel-vnet"
  resource_group_name  = "DefaultResourceGroup-CNE2-chinanorth3"
}

data "azurerm_subnet" "demo4_subnet" {
  name                 = "demo4subnet"
  virtual_network_name = "pip3-internel-vnet"
  resource_group_name  = "DefaultResourceGroup-CNE2-chinanorth3"
}
