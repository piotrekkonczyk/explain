from ollama import Client
from typer import Typer
from rich.console import Console
from rich.markdown import Markdown

from src.commands import answer

app = Typer()

client = Client()
model = "llama3"

console = Console()


@app.command()
def ask(question: str):
    response = answer(client=client, model=model, question=question)

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


@app.command()
def docstring(function: str):
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Your goal will be to generate a docstring for provided function. Always assume that API's that are used inside the function are valid and try to understand them also. Describe the function, parameters and what it returns",
            },
            {"role": "user", "content": function},
        ],
    )

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


if __name__ == "__main__":
    app()
