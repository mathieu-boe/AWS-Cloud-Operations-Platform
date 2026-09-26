from cloudops.health_checks.runner import HealthCheckRunner
from cloudops.health_checks.static import StaticHealthCheck


def test_runner_executes_all_health_checks() -> None:
    runner = HealthCheckRunner(
        [
            StaticHealthCheck(service="lambda"),
            StaticHealthCheck(service="dynamodb"),
            StaticHealthCheck(service="s3"),
        ]
    )

    results = runner.run()

    assert len(results) == 3
    assert results[0].service == "lambda"
    assert results[1].service == "dynamodb"
    assert results[2].service == "s3"


def test_runner_returns_healthy_results() -> None:
    runner = HealthCheckRunner(
        [
            StaticHealthCheck(service="lambda"),
            StaticHealthCheck(service="s3"),
        ]
    )

    results = runner.run()

    assert all(result.status == "healthy" for result in results)
