# terraform/main.tf

terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}

resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo Hello, Terraform!"
  }
}
