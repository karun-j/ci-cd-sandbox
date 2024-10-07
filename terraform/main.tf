terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}

# Define a simple resource just for testing
resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo Hello, Terraform!"
  }
}
