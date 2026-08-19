resource "aws_cloudwatch_log_group" "collector" {
  name              = "/aws/lambda/${var.project_name}-${var.environment}-collector"
  retention_in_days = 30
}
