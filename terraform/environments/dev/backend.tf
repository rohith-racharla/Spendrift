terraform {
  backend "s3" {
    bucket       = "${var.project_name}-tfstate"
    key          = "dev/terraform.tfstate"
    region       = var.region
    profile      = var.aws_profile
    use_lockfile = true
  }
}
