from ollama import Client, ChatResponse

from src.get_prompts import (
    ASK_PROMPT,
    DOCSTRING_PROMPT,
    REFACTOR_PROMPT,
    SUGGEST_TESTS_PROMPT,
    SUMMARIZE_PROMPT,
)


def answer(client: Client, question: str) -> ChatResponse:
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": ASK_PROMPT + "\n" + question,
            },
        ],
    )

    return response


def generate_docstring(client: Client, function: str) -> ChatResponse:
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": DOCSTRING_PROMPT + "\n" + function,
            },
        ],
    )

    return response


def refactor_code(client: Client, code: str) -> ChatResponse:
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": REFACTOR_PROMPT + "\n" + code,
            },
        ],
    )

    return response


def summarize_file(client: Client, file_path: str):
    with open(file_path) as file:
        file_content = file.read()

        response = client.chat(
            messages=[
                {
                    "role": "user",
                    "content": SUMMARIZE_PROMPT + "\n" + file_content,
                },
            ],
        )

        return response


def suggest_tests(client: Client, function: str) -> ChatResponse:
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": SUGGEST_TESTS_PROMPT + "\n" + function,
            },
        ],
    )

    return response
