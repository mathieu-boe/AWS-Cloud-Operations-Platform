terraform {
  required_version = ">= 1.16, < 2.0"

  required_providers {
    aws = {
      source = "hashicorp/aws"
    }

    archive = {
      source = "hashicorp/archive"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}
