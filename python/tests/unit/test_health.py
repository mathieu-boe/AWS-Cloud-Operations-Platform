from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from cloudops.models.health import HealthResult


def test_health_result_creates_valid_result() -> None:
    result = HealthResult(
        service="lambda",
        status="healthy",
        latency_ms=42.5,
        message="Lambda responded successfully",
    )

    assert result.service == "lambda"
    assert result.status == "healthy"
    assert result.latency_ms == 42.5
    assert result.message == "Lambda responded successfully"
    assert result.timestamp.tzinfo == UTC


def test_health_result_rejects_negative_latency() -> None:
    with pytest.raises(ValidationError):
        HealthResult(
            service="lambda",
            status="healthy",
            latency_ms=-1,
        )


def test_health_result_accepts_explicit_timestamp() -> None:
    timestamp = datetime(2026, 1, 1, tzinfo=UTC)

    result = HealthResult(
        service="dynamodb",
        status="healthy",
        latency_ms=10,
        timestamp=timestamp,
    )

    assert result.timestamp == timestamp
