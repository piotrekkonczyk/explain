import ollama
import typer

app = typer.Typer()

client = ollama.Client()
model = "llama3"


@app.command()
def ask(question: str):
    response = client.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": "Your goal will be to answer the given question",
            },
            {"role": "user", "content": question},
        ],
    )

    print(response.message.content)


if __name__ == "__main__":
    app()
