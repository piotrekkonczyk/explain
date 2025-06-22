from ollama import Client, ChatResponse


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
