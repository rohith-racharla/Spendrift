terraform {
  backend "s3" {
    bucket       = "aws-cost-anomaly-detector-tfstate"
    key          = "dev/terraform.tfstate"
    region       = "us-east-1"
    profile      = "finops-dev"
    use_lockfile = true
  }
}
