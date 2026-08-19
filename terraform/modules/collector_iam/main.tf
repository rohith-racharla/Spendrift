resource "aws_iam_role" "collector" {
  name = "${var.project_name}-${var.environment}-collector"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "lambda.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "collector" {
  name = "${var.project_name}-${var.environment}-collector-policy"
  role = aws_iam_role.collector.id

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Sid    = "CostExplorerRead"
        Effect = "Allow"

        Action = [
          "ce:GetCostAndUsage"
        ]

        Resource = "*"
      },

      {
        Sid    = "RawCostDataWrite"
        Effect = "Allow"

        Action = [
          "s3:PutObject"
        ]

        Resource = "${var.raw_cost_bucket_arn}/*"
      },

      {
        Sid    = "RawCostBucketMetadata"
        Effect = "Allow"

        Action = [
          "s3:GetBucketLocation"
        ]

        Resource = var.raw_cost_bucket_arn
      },

      {
        Sid    = "CloudWatchLogs"
        Effect = "Allow"

        Action = [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]

        Resource = "${var.log_group_arn}:*"
      }
    ]
  })
}
