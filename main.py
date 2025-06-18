from ollama import Client
from typer import Typer
from rich.console import Console
from rich.markdown import Markdown


app = Typer()

client = Client()
model = "llama3"

console = Console()


@app.command()
def ask(question: str):
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

    if not response.message.content:
        raise Exception("There was an error while generating a response")

    markdown_content = Markdown(response.message.content)
    console.print(markdown_content)


if __name__ == "__main__":
    app()
