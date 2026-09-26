from cloudops.health_checks.base import HealthCheck
from cloudops.models.health import HealthResult


class HealthCheckRunner:
    """Run a collection of health checks and collect their results."""

    def __init__(self, checks: list[HealthCheck]) -> None:
        self.checks = checks

    def run(self) -> list[HealthResult]:
        return [check.check() for check in self.checks]
