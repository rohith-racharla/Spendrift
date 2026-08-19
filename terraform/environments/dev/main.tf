resource "aws_s3_bucket" "raw_cost_data" {
  bucket = "${var.project_name}-${var.environment}-cost-data"
}

resource "aws_s3_bucket_versioning" "raw_cost_data" {
  bucket = aws_s3_bucket.raw_cost_data.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_public_access_block" "raw_cost_data" {
  bucket = aws_s3_bucket.raw_cost_data.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "raw_cost_data" {
  bucket = aws_s3_bucket.raw_cost_data.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
