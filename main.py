from ollama import chat
import typer


def main(message: str):
    response = chat(model="llama3", messages=[{"role": "user", "content": message}])

    print(response.message)


if __name__ == "__main__":
    typer.run(main)
