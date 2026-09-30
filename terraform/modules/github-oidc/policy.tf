data "aws_caller_identity" "current" {}

variable "aws_region" {
  description = "AWS region used by the Lambda infrastructure."
  type        = string
}

resource "aws_iam_policy" "terraform_lambda" {
  name        = "GitHubActions-Terraform-Lambda"
  description = "Scoped Terraform permissions for GitHub Actions Lambda infrastructure"

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Sid    = "LambdaManagement"
        Effect = "Allow"

        Action = [
          "lambda:CreateFunction",
          "lambda:DeleteFunction",
          "lambda:GetFunction",
          "lambda:GetFunctionConfiguration",
          "lambda:UpdateFunctionCode",
          "lambda:UpdateFunctionConfiguration",
          "lambda:TagResource",
          "lambda:UntagResource",
          "lambda:ListTags"
        ]

        Resource = "arn:aws:lambda:${var.aws_region}:${data.aws_caller_identity.current.account_id}:function:${var.lambda_function_name}"
      },
      {
        Sid    = "IamRoleManagement"
        Effect = "Allow"

        Action = [
          "iam:CreateRole",
          "iam:DeleteRole",
          "iam:GetRole",
          "iam:TagRole",
          "iam:UntagRole",
          "iam:ListRoleTags",
          "iam:ListAttachedRolePolicies",
          "iam:AttachRolePolicy",
          "iam:DetachRolePolicy",
          "iam:GetPolicy",
          "iam:GetPolicyVersion"
        ]

        Resource = [
          "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/${var.lambda_execution_role_name}"
        ]
      },
      {
        Sid    = "PassLambdaExecutionRole"
        Effect = "Allow"

        Action = [
          "iam:PassRole"
        ]

        Resource = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/${var.lambda_execution_role_name}"
      },
      {
        Sid    = "ReadAccountInformation"
        Effect = "Allow"

        Action = [
          "sts:GetCallerIdentity",
          "iam:ListRoles",
          "iam:ListPolicies"
        ]

        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "terraform_lambda" {
  role       = aws_iam_role.github_actions.name
  policy_arn = aws_iam_policy.terraform_lambda.arn
}
