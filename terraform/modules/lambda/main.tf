resource "aws_lambda_function" "this" {
  function_name = var.function_name
  role          = aws_iam_role.this.arn
  handler       = "handler.handler"
  runtime       = "python3.14"

  filename         = var.filename
  source_code_hash = filebase64sha256(var.filename)

  tags = {
    Project     = "AWS-Cloud-Operations-Platform"
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}