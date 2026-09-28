from time import perf_counter

import boto3

from cloudops.health_checks.base import HealthCheck
from cloudops.models.health import HealthResult


class LambdaHealthCheck(HealthCheck):
    """Check the accessibility of an AWS Lambda function."""

    #def __init__(self, function_name: str) -> None:
    def __init__(self, function_name: str, region_name: str) -> None:
        self.function_name = function_name
        #self.client = boto3.client("lambda")
        self.client = boto3.client("lambda", region_name=region_name)

    def check(self) -> HealthResult:
        start = perf_counter()

        try:
            self.client.get_function(FunctionName=self.function_name)

            return HealthResult(
                service="lambda",
                status="healthy",
                latency_ms=(perf_counter() - start) * 1000,
                message=f"Lambda function '{self.function_name}' is accessible",
            )

        except Exception as exc:
            return HealthResult(
                service="lambda",
                status="unhealthy",
                latency_ms=(perf_counter() - start) * 1000,
                message=str(exc),
            )
