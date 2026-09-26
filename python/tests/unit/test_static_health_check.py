from cloudops.health_checks.static import StaticHealthCheck


def test_static_health_check_returns_healthy_result() -> None:
    check = StaticHealthCheck()

    result = check.check()

    assert result.service == "local"
    assert result.status == "healthy"
    assert result.latency_ms == 0
    assert result.message == "Local health check succeeded"


def test_static_health_check_supports_custom_service_name() -> None:
    check = StaticHealthCheck(service="test-service")

    result = check.check()

    assert result.service == "test-service"
    assert result.status == "healthy"
