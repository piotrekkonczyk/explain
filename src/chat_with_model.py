from ollama import ChatResponse, Client
from src.constants import MODEL


def chat_with_model(client: Client, prompt: str, content: str) -> ChatResponse:
    response = client.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt + "\n" + content,
            },
        ],
    )

    return response
