
from dataclasses import dataclass


@dataclass
class ProviderConfig:
    name: str
    provider_type: str
    base_url: str | None = None
    api_key_env: str | None = None


@dataclass
class WorkerModelConfig:
    provider: str
    model: str
    temperature: float = 0.2


# Available providers
PROVIDERS = {
    "gemini": ProviderConfig(
        name="Gemini",
        provider_type="openai_compatible",
        base_url=None,
        api_key_env="GEMINI_API_KEY"
    ),
}


# Model assignments
WORKER_MODELS = {
    "planner": None,
    "researcher": None,

    "developer": WorkerModelConfig(
        provider="gemini",
        model="gemini-3.5-flash-lite",
        temperature=0.2
    ),

    "tester": None,
    "reviewer": None,
}