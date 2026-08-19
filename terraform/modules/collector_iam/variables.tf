variable "project_name" {
  description = "Project name."
  type        = string
}

variable "environment" {
  description = "Deployment environment."
  type        = string
}

variable "raw_cost_bucket_arn" {
  description = "ARN of the S3 bucket where raw cost data is stored."
  type        = string
}

variable "log_group_arn" {
  description = "ARN of the Lambda CloudWatch log group."
  type        = string
}
