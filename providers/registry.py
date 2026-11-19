from providers.base import BaseProvider


class ProviderRegistry:

    def __init__(self):
        self._providers: dict[str, BaseProvider] = {}

    def register(self, name: str, provider: BaseProvider):
        if name in self._providers:
            raise ValueError(f"Provider '{name}' is already registered.")

        self._providers[name] = provider

    def get(self, name: str) -> BaseProvider:
        if name not in self._providers:
            raise ValueError(f"Provider '{name}' is not registered.")

        return self._providers[name]

    def list_providers(self) -> list[str]:
        return list(self._providers.keys())