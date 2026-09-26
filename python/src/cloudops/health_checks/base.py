from abc import ABC, abstractmethod

from cloudops.models.health import HealthResult


class HealthCheck(ABC):
    """Base interface for all service health checks."""

    @abstractmethod
    def check(self) -> HealthResult:
        """Check service health and return the result."""
        raise NotImplementedError
