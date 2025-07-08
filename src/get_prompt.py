def get_prompt(file_path: str):
    with open(file_path) as file:
        return file.read()
