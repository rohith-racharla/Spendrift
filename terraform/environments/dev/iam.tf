module "collector_iam" {
  source = "../../modules/collector_iam"

  project_name = var.project_name
  environment  = var.environment

  raw_cost_bucket_arn = aws_s3_bucket.raw_cost_data.arn
  log_group_arn       = aws_cloudwatch_log_group.collector.arn
}
