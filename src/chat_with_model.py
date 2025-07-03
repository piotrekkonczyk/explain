from ollama import ChatResponse, Client
from src.constants import MODEL


def chat_with_model(
    client: Client, prompt: str, content: str, description: str | None = None
) -> ChatResponse:
    user_prompt = prompt

    if description:
        user_prompt += f"The user has also requested to {description.strip()}"

    response = client.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": user_prompt},
            {"role": "user", "content": content},
        ],
    )

    return response
