provider "aws" {
  region  = "us-east-1"
  profile = "terraform"
}

terraform {

  backend "local" {
    path = "terraform.tfstate"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.66"
    }
  }
}

