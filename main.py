from ollama import Client
from typer import Typer, Option
from rich.console import Console

from src.commands import (
    answer,
    generate_docstring,
    refactor_code,
    suggest_tests,
    summarize_file,
)
from src.utils import get_file_content, print_with_markdown, verify_message_content

app = Typer()

client = Client()

console = Console()


@app.command()
def ask(question: str):
    response = answer(client=client, question=question)
    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command()
def docstring(
    input: str = "",
    file: str = Option(None, "--file", "-f"),
    description: str = Option(None, "--description", "-d"),
):
    content = get_file_content(file_path=file) if file else input
    response = generate_docstring(client=client, input=content, description=description)

    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command()
def refactor(input: str, file: bool = False):
    if file:
        file_content = get_file_content(input)
        response = refactor_code(client=client, input=file_content)
    else:
        response = refactor_code(client=client, input=input)

    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command()
def summarize(path: str):
    response = summarize_file(client=client, file_path=path)
    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command()
def tests(input: str, file: bool = False):
    if file:
        file_content = get_file_content(input)
        response = suggest_tests(client=client, input=file_content)
    else:
        response = suggest_tests(client=client, input=input)

    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


if __name__ == "__main__":
    app()
