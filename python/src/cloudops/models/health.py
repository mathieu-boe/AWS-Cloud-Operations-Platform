from datetime import UTC, datetime

from pydantic import BaseModel, Field


class HealthResult(BaseModel):
    service: str
    status: str
    latency_ms: float = Field(ge=0)
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )
    message: str | None = None
