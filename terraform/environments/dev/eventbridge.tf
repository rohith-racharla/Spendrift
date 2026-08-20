resource "aws_cloudwatch_event_rule" "daily_cost_collection" {
  name = "${var.project_name}-${var.environment}-daily-cost-collection"

  description = "Triggers the daily AWS cost collector"

  schedule_expression = "cron(0 1 * * ? *)"
}

resource "aws_cloudwatch_event_target" "collector" {
  rule = aws_cloudwatch_event_rule.daily_cost_collection.name

  target_id = "cost-collector"

  arn = aws_lambda_function.collector.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id = "AllowEventBridgeInvoke"

  action = "lambda:InvokeFunction"

  function_name = aws_lambda_function.collector.function_name

  principal = "events.amazonaws.com"

  source_arn = aws_cloudwatch_event_rule.daily_cost_collection.arn
}
