from ollama import Client, ChatResponse

from src.get_prompts import ASK_PROMPT, DOCSTRING_PROMPT, REFACTOR_PROMPT


def answer(client: Client, model: str, question: str) -> ChatResponse:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": ASK_PROMPT + "\n" + question,
            },
        ],
    )

    return response


def generate_docstring(client: Client, model: str, function: str) -> ChatResponse:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": DOCSTRING_PROMPT + "\n" + function,
            },
        ],
    )

    return response


def refactor_code(client: Client, model: str, code: str) -> ChatResponse:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": REFACTOR_PROMPT + "\n" + code,
            },
        ],
    )

    return response
