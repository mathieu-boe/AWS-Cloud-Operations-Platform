from cloudops.health_checks.base import HealthCheck
from cloudops.models.health import HealthResult


class StaticHealthCheck(HealthCheck):
    """Simple health check used for local development and testing."""

    def __init__(self, service: str = "local") -> None:
        self.service = service

    def check(self) -> HealthResult:
        return HealthResult(
            service=self.service,
            status="healthy",
            latency_ms=0,
            message="Local health check succeeded",
        )
