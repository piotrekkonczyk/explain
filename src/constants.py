from enum import Enum
from src.get_prompt import get_prompt

MODEL = "qwen2.5-coder"


class PROMPTS(Enum):
    ASK_PROMPT = get_prompt("prompts/ask.txt")
    DOCSTRING_PROMPT = get_prompt("prompts/docstring.txt")
    REFACTOR_PROMPT = get_prompt("prompts/refactor.txt")
    SUMMARIZE_PROMPT = get_prompt("prompts/summarize_file.txt")
    SUGGEST_TESTS_PROMPT = get_prompt("prompts/suggest_tests.txt")
