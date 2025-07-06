from ollama import Client
from typer import Argument, Typer, Option
from rich.console import Console

from src.commands import summarize_file
from src.get_prompts import (
    DOCSTRING_PROMPT,
    PROMPTS,
    REFACTOR_PROMPT,
    SUGGEST_TESTS_PROMPT,
)
from src.chat_with_model import chat_with_model
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
    model: str = Option(
        None,
        "--model",
        "-m",
        help=(
            "Optional name of the LLM to use (e.g., 'llama3', 'qwen2.5-coder', 'codellama:13b'). "
            "Defaults to the model configured globally or in your client."
        ),
    ),
):
    response = chat_with_model(
        client=client,
        prompt=PROMPTS.ASK_PROMPT.value,
        content=question,
        description=description,
        model=model,
    )
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
    model: str = Option(
        None,
        "--model",
        "-m",
        help=(
            "Optional name of the LLM to use (e.g., 'llama3', 'qwen2.5-coder', 'codellama:13b'). "
            "Defaults to the model configured globally or in your client."
        ),
    ),
):
    content = get_file_content(file_path=file) if file else code
    response = chat_with_model(
        client=client,
        prompt=DOCSTRING_PROMPT,
        content=content,
        description=description,
        model=model,
    )

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
    model: str = Option(
        None,
        "--model",
        "-m",
        help=(
            "Optional name of the LLM to use (e.g., 'llama3', 'qwen2.5-coder', 'codellama:13b'). "
            "Defaults to the model configured globally or in your client."
        ),
    ),
):
    content = get_file_content(file_path=file) if file else code

    response = chat_with_model(
        client=client,
        prompt=REFACTOR_PROMPT,
        content=content,
        description=description,
        model=model,
    )

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
    model: str = Option(
        None,
        "--model",
        "-m",
        help=(
            "Optional name of the LLM to use (e.g., 'llama3', 'qwen2.5-coder', 'codellama:13b'). "
            "Defaults to the model configured globally or in your client."
        ),
    ),
):
    response = summarize_file(
        client=client, file_path=file, description=description, model=model
    )
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
    model: str = Option(
        None,
        "--model",
        "-m",
        help=(
            "Optional name of the LLM to use (e.g., 'llama3', 'qwen2.5-coder', 'codellama:13b'). "
            "Defaults to the model configured globally or in your client."
        ),
    ),
):
    content = get_file_content(file) if file else code
    response = chat_with_model(
        client=client,
        prompt=SUGGEST_TESTS_PROMPT,
        content=content,
        description=description,
        model=model,
    )

    message_content = verify_message_content(response.message.content)

    print_with_markdown(console=console, message_content=message_content)


if __name__ == "__main__":
    app()
