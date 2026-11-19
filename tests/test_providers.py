
from unittest.mock import patch

from providers.factory import build_provider_registry
from providers.resolver import ModelResolver


def test_provider_initialization():
    with patch.dict("os.environ", {
        "QWEN_API_KEY": "test-api-key",
        "QWEN_BASE_URL": "https://example.com/v1"
    }):
        registry = build_provider_registry()

    assert "qwen" in registry.list_providers()


def test_model_resolver():
    with patch.dict("os.environ", {
        "QWEN_API_KEY": "test-api-key",
        "QWEN_BASE_URL": "https://example.com/v1"
    }):
        registry = build_provider_registry()

    resolver = ModelResolver(registry)

    model = resolver.get_model("developer")

    assert model is not None
