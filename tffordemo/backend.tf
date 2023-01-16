terraform {
  # required_version = ">= 0.12.0"  
  #  backend "azurerm" { }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.15.0"
    }
  }
}
