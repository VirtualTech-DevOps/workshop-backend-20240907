terraform {
  required_version = "~> 1.5.0"

  required_providers {
    nifcloud = {
      source  = "nifcloud/nifcloud"
      version = "~> 1.9.0"
    }
  }
}
