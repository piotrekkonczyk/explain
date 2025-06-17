from ollama import chat


def main():
    response = chat(
        model="llama3", messages=[{"role": "user", "content": "How are you doing?"}]
    )

    print(response.message)


if __name__ == "__main__":
    main()
