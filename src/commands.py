from ollama import Client, ChatResponse

from src.get_prompts import DOCSTRING_PROMPT


def answer(client: Client, model: str, question: str) -> ChatResponse:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Your goal will be to answer the given question",
            },
            {"role": "user", "content": question},
        ],
    )

    return response


def generate_docstring(client: Client, model: str, function: str) -> ChatResponse:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": DOCSTRING_PROMPT + function,
            },
        ],
    )

    return response
