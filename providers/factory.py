import os
from dotenv import load_dotenv

load_dotenv()
from providers.config import PROVIDERS
from providers.registry import ProviderRegistry
from providers.adapters.openai_compatible import OpenAICompatibleProvider


def build_provider_registry() -> ProviderRegistry:
    registry = ProviderRegistry()

    for key, config in PROVIDERS.items():

        if config.provider_type == "openai_compatible":
            base_url = (
                config.base_url
                or os.getenv(f"{key.upper()}_BASE_URL")
            )

            api_key = (
                os.getenv(config.api_key_env)
                if config.api_key_env
                else None
            )

            if not base_url:
                raise ValueError(
                    f"Missing base URL for provider '{key}'."
                )

            if not api_key:
                raise ValueError(
                    f"Missing API key for provider '{key}'."
                )

            provider = OpenAICompatibleProvider(
                base_url=base_url,
                api_key=api_key
            )

            registry.register(key, provider)

        else:
            raise ValueError(
                f"Unsupported provider type: {config.provider_type}"
            )

    return registry