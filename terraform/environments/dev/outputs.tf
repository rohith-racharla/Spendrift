output "raw_cost_bucket_name" {
  description = "S3 bucket used for raw AWS cost data."
  value       = aws_s3_bucket.raw_cost_data.bucket
}

output "collector_role_arn" {
  description = "IAM role ARN for the cost collector."
  value       = module.collector_iam.role_arn
}

output "collector_log_group" {
  description = "CloudWatch log group for the cost collector."
  value       = aws_cloudwatch_log_group.collector.name
}
