from abc import ABC, abstractmethod
from langchain_core.language_models.chat_models import BaseChatModel


class BaseProvider(ABC):

    @abstractmethod
    def create_chat_model(
        self,
        model: str,
        **kwargs
    ) -> BaseChatModel:
        """Create and return a configured chat model."""
        pass