data "archive_file" "lambda" {
  type        = "zip"
  source_file = "${path.module}/lambda/handler.py"
  output_path = "${path.module}/lambda/handler.zip"
}

module "lambda" {
  source = "../../modules/lambda"

  function_name = "cloudops-health"
  filename      = data.archive_file.lambda.output_path
}
