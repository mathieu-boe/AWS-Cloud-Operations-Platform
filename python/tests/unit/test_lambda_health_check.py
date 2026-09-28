import io
import zipfile

import boto3
from moto import mock_aws

from cloudops.config import Settings
from cloudops.health_checks.lambda_check import LambdaHealthCheck


def create_lambda_zip() -> bytes:
    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr(
            "handler.py",
            "def handler(event, context):\n    return {'statusCode': 200}\n",
        )

    return buffer.getvalue()


@mock_aws
def test_lambda_health_check_reports_healthy_function() -> None:
    iam_client = boto3.client("iam", region_name="eu-west-2")
    iam_client.create_role(
        RoleName="test-role",
        AssumeRolePolicyDocument="{}",
    )

    lambda_client = boto3.client("lambda", region_name="eu-west-2")

    lambda_client.create_function(
        FunctionName="cloudops-health",
        Runtime="python3.14",
        Role="arn:aws:iam::123456789012:role/test-role",
        Handler="handler.handler",
        Code={"ZipFile": create_lambda_zip()},
    )

    settings = Settings()

    #check = LambdaHealthCheck(function_name="cloudops-health")
    check = LambdaHealthCheck(
        function_name="cloudops-health",
        region_name=settings.aws_region,
    )

    result = check.check()

    assert result.service == "lambda"
    assert result.status == "healthy"
    assert result.latency_ms >= 0


@mock_aws
def test_lambda_health_check_reports_missing_function_as_unhealthy() -> None:
    settings = Settings()

    #check = LambdaHealthCheck(function_name="does-not-exist")
    check = LambdaHealthCheck(
        function_name="does-not-exist",
        region_name=settings.aws_region,
    )

    result = check.check()

    assert result.service == "lambda"
    assert result.status == "unhealthy"
    assert result.latency_ms >= 0
    assert result.message is not None
