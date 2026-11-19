
from providers.config import WORKER_MODELS
from providers.registry import ProviderRegistry


class ModelResolver:

    def __init__(self, registry: ProviderRegistry):
        self.registry = registry

    def get_model(self, worker_name: str):
        config = WORKER_MODELS.get(worker_name)

        if config is None:
            return None

        provider = self.registry.get(config.provider)

        return provider.create_chat_model(
            model=config.model,
            temperature=config.temperature
        )
