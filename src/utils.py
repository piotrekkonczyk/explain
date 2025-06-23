from rich.console import Console
from rich.markdown import Markdown


def verify_message_content(message_content: str | None) -> str:
    if not message_content:
        raise Exception("There was an error while generating a response")

    return message_content


def print_with_markdown(console: Console, message_content: str) -> None:
    markdown_content = Markdown(message_content)

    console.print(markdown_content)
