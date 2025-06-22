from ollama import Client
from typer import Typer
from rich.console import Console
from rich.markdown import Markdown

from src.get_prompts import get_prompt
from src.commands import answer, generate_docstring

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
    response = generate_docstring(client=client, model=model, function=function)

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


if __name__ == "__main__":
    app()
