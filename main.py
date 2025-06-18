import ollama
import typer

app = typer.Typer()


@app.command()
def ask(question: str):
    response = ollama.chat(
        model="llama3", messages=[{"role": "user", "content": question}]
    )

    print(response.message.content)


def main(message: str):
    response = ollama.chat(
        model="llama3", messages=[{"role": "user", "content": message}]
    )

    print(response.message)


if __name__ == "__main__":
    app()
