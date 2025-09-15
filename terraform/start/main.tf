terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "random" {}

resource "random_pet" "name" {
  length = 2
}

output "pet_name" {
  value = random_pet.name.id
}