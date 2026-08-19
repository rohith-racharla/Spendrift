variable "aws_region" {
  description = "AWS region where the project infrastructure will be deployed."
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "AWS CLI profile used by Terraform."
  type        = string
  default     = "finops-dev"
}

variable "project_name" {
  description = "Project name used for resource naming and tagging."
  type        = string
  default     = "aws-cost-anomaly-detector"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}
