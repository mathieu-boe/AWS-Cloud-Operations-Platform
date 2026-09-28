from cloudops.config import Settings


def test_settings_use_london_as_default_region() -> None:
    settings = Settings()

    assert settings.aws_region == "eu-west-2"


def test_settings_accept_custom_region() -> None:
    settings = Settings(aws_region="us-east-1")

    assert settings.aws_region == "us-east-1"
