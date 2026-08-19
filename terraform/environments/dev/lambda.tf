data "archive_file" "collector" {
  type        = "zip"
  source_dir  = "${path.root}/../../../build/lambda"
  output_path = "${path.root}/../../../build/collector.zip"
}

resource "aws_lambda_function" "collector" {
  function_name = "${var.project_name}-${var.environment}-collector"

  role = module.collector_iam.role_arn

  runtime = "python3.12"
  handler = "collector.handler.lambda_handler"

  filename         = data.archive_file.collector.output_path
  source_code_hash = data.archive_file.collector.output_base64sha256

  timeout     = 60
  memory_size = 256

  environment {
    variables = {
      RAW_COST_BUCKET_NAME = aws_s3_bucket.raw_cost_data.bucket
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.collector
  ]
}
