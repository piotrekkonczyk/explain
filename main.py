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

app = Typer(no_args_is_help=True)

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
    response = answer(client=client, question=question, description=description)
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


@app.command(help="Refactor Python code blocks or entire files to improve quality.")
def refactor(
    code: str = Option(
        None,
        "--code",
        "-c",
        help="Inline Python code to be refactored.",
    ),
    file: str = Option(
        None,
        "--file",
        "-f",
        help="Path to a file to be refactored.",
    ),
    description: str = Option(
        None,
        "--description",
        "-d",
        help="Additional instruction to guide the refactor (e.g., 'simplify loop', 'use list comprehension').",
    ),
):
    content = get_file_content(file_path=file) if file else code
    response = refactor_code(client=client, input=content, description=description)

    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command(help="Summarize the purpose and structure of a Python file.")
def summarize(
    file: str = Option(
        ...,
        "--file",
        "-f",
        help="Path to the Python file that should be summarized.",
    ),
    description: str = Option(
        None,
        "--description",
        "-d",
        help="Optional extra instruction for the model (e.g., 'focus on data models only').",
    ),
):
    response = summarize_file(client=client, file_path=file, description=description)
    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


@app.command(help="Generate pytest tests for a Python function or file.")
def tests(
    code: str = Option(
        None,
        "--code",
        "-c",
        help="Inline Python function to generate tests for.",
    ),
    file: str = Option(
        None,
        "--file",
        "-f",
        help="Path to a Python file for which to generate tests.",
    ),
    description: str = Option(
        None,
        "--description",
        "-d",
        help="Optional instruction to guide test generation (e.g., 'focus on edge cases', 'assume high I/O volume').",
    ),
):
    content = get_file_content(file) if file else code
    response = suggest_tests(client=client, input=content, description=description)

    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


if __name__ == "__main__":
    app()
