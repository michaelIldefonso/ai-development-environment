from langchain_openai import ChatOpenAI

from providers.base import BaseProvider


class OpenAICompatibleProvider(BaseProvider):

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def create_chat_model(
        self,
        model: str,
        **kwargs
    ) -> ChatOpenAI:

        return ChatOpenAI(
            model=model,
            base_url=self.base_url,
            api_key=self.api_key,
            **kwargs
        )