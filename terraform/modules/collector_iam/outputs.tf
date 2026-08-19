output "role_arn" {
  description = "ARN of the IAM role used by the cost collector Lambda."
  value       = aws_iam_role.collector.arn
}

output "role_name" {
  description = "Name of the IAM role used by the cost collector Lambda."
  value       = aws_iam_role.collector.name
}
