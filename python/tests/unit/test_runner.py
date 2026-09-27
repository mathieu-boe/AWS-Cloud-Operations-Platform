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


def test_runner_converts_check_exception_to_unhealthy_result() -> None:
    class FailingHealthCheck:
        def check(self):
            raise RuntimeError("Simulated service failure")

    runner = HealthCheckRunner([FailingHealthCheck()])

    results = runner.run()

    assert len(results) == 1
    assert results[0].status == "unhealthy"
    assert "Simulated service failure" in (results[0].message or "")


def test_runner_continues_after_failed_check() -> None:
    class FailingHealthCheck:
        def check(self):
            raise RuntimeError("Simulated failure")

    runner = HealthCheckRunner(
        [
            StaticHealthCheck(service="lambda"),
            FailingHealthCheck(),
            StaticHealthCheck(service="s3"),
        ]
    )

    results = runner.run()

    assert len(results) == 3
    assert results[0].status == "healthy"
    assert results[1].status == "unhealthy"
    assert results[2].status == "healthy"
