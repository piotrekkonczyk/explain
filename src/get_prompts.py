def get_prompt(file_path: str):
    with open(file_path) as file:
        return file.read()


ASK_PROMPT = get_prompt("prompts/ask.txt")
DOCSTRING_PROMPT = get_prompt("prompts/docstring.txt")
