from ollama import ChatResponse, Client
from src.constants import MODEL


def chat_with_model(
    client: Client,
    prompt: str,
    content: str,
    description: str | None = None,
    model: str | None = None,
) -> ChatResponse:
    if description:
        content += f"I would also like you to {description.strip()}"
        prompt += f"I would also like you to {description.strip()}"

    response = client.chat(
        model=model if model else MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
    )

    return response
