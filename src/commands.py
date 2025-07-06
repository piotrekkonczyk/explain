from ollama import Client, ChatResponse

from src.get_prompts import PROMPTS
from src.constants import MODEL
from src.chat_with_model import chat_with_model


def summarize_file(
    client: Client, file_path: str, description: str | None = None, model: str = MODEL
) -> ChatResponse:
    with open(file_path) as file:
        file_content = file.read()

        return chat_with_model(
            client=client,
            prompt=PROMPTS.SUMMARIZE_PROMPT.value,
            content=file_content,
            description=description,
            model=model,
        )
