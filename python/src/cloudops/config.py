from pydantic import BaseModel


class Settings(BaseModel):
    """Application configuration."""

    aws_region: str = "eu-west-2"
