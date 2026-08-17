variable "aws_region" {
  description = "AWS region for Terraform state infrastructure."
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "AWS CLI profile used by Terraform."
  type        = string
  default     = "finops-dev"
}

variable "project_name" {
  description = "Project name."
  type        = string
  default     = "aws-cost-anomaly-detector"
}
