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


def generate_docstring(client: Client, model: str, function: str) -> ChatResponse:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Generate a combination of docstring and provided function. Always assume that API's that are used inside the given function are valid and try to understand them also. Describe the function, parameters, simple usage and what it returns. The output should look like this: a combined function, containing docstring and code. You will always be given the wrapper function, so describe it, not the API's used inside. If return type is explicitly given, use it instead of defaults like dicts etc. Output the function in ```python``` markdown block."
                + function,
            },
        ],
    )

    return response
