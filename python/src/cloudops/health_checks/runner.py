from time import perf_counter

from cloudops.health_checks.base import HealthCheck
from cloudops.models.health import HealthResult


class HealthCheckRunner:
    """Run a collection of health checks and collect their results."""

    def __init__(self, checks: list[HealthCheck]) -> None:
        self.checks = checks

    def run(self) -> list[HealthResult]:
        results: list[HealthResult] = []

        for check in self.checks:
            start = perf_counter()

            try:
                result = check.check()
            except Exception as exc:
                latency_ms = (perf_counter() - start) * 1000
                result = HealthResult(
                    service=type(check).__name__,
                    status="unhealthy",
                    latency_ms=latency_ms,
                    message=str(exc),
                )

            results.append(result)

        return results
