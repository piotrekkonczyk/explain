from ollama import Client
from typer import Argument, Typer, Option
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


@app.command(help="Ask a programming or software-related question.")
def ask(
    question: str = Argument(
        "",
        help="A programming-related question the model should answer.",
        show_default=False,
    ),
    description: str = Option(
        None,
        "--description",
        "-d",
        help="Additional context or intent to help refine the model's answer.",
    ),
):
    response = answer(client=client, question=question)
    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command(help="Add docstrings to python code blocks or entire files.")
def docstring(
    code: str = Option(
        None,
        "--code",
        "-c",
        help="Content of the function that model will try to document.",
    ),
    file: str = Option(
        None, "--file", "-f", help="Path to file that should be documented."
    ),
    description: str = Option(
        None,
        "--description",
        "-d",
        help="Additional description to precise what the model should focus on.",
    ),
):
    content = get_file_content(file_path=file) if file else code
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
