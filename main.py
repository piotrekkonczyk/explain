from ollama import Client
from typer import Typer
from rich.console import Console
from rich.markdown import Markdown

from src.commands import (
    answer,
    generate_docstring,
    refactor_code,
    suggest_tests,
    summarize_file,
)
from src.utils import print_with_markdown, verify_message_content

app = Typer()

client = Client()

console = Console()


@app.command()
def ask(question: str):
    response = answer(client=client, question=question)
    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command()
def docstring(function: str):
    response = generate_docstring(client=client, function=function)

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


@app.command()
def refactor(code: str):
    response = refactor_code(client=client, code=code)

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


@app.command()
def summarize(path: str):
    response = summarize_file(client=client, file_path=path)

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


@app.command()
def tests(function: str):
    response = suggest_tests(client=client, function=function)

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


if __name__ == "__main__":
    app()
