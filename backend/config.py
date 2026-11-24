from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Eventia"
    app_env: str = "development"
    secret_key: str = "development-only-change-me"
    postgres_url: str = "postgresql://localhost:5432/eventia_users"
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_database: str = "eventia_management"
    frontend_url: str = "http://localhost:8501"
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_id_premium: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
