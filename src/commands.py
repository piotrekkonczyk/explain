from ollama import Client, ChatResponse

from src.chat_with_model import chat_with_model
from src.get_prompts import (
    ASK_PROMPT,
    DOCSTRING_PROMPT,
    REFACTOR_PROMPT,
    SUGGEST_TESTS_PROMPT,
    SUMMARIZE_PROMPT,
)


def answer(client: Client, question: str) -> ChatResponse:
    return chat_with_model(client=client, prompt=ASK_PROMPT, content=question)


def generate_docstring(
    client: Client, input: str, description: str | None = None
) -> ChatResponse:
    return chat_with_model(
        client=client, prompt=DOCSTRING_PROMPT, content=input, description=description
    )


def refactor_code(
    client: Client, input: str, description: str | None = None
) -> ChatResponse:
    return chat_with_model(
        client=client, prompt=REFACTOR_PROMPT, content=input, description=description
    )


def summarize_file(client: Client, file_path: str, description: str | None = None):
    with open(file_path) as file:
        file_content = file.read()

        return chat_with_model(
            client=client,
            prompt=SUMMARIZE_PROMPT,
            content=file_content,
            description=description,
        )


def suggest_tests(client: Client, input: str) -> ChatResponse:
    return chat_with_model(client=client, prompt=SUGGEST_TESTS_PROMPT, content=input)
