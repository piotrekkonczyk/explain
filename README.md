# explain

small CLI tool for working with local LLMs via [ollama](https://ollama.com)

you can use it to:

- add docstrings to functions or files
- refactor code
- generate tests (pytest)
- summarize a file
- ask programming-related questions

built with Python, Typer, and Rich  
tested mostly with `llama3` and `qwen2.5-coder`

---

## install

```bash
poetry install
```

```bash
# build binary (optional):
pyinstaller --onefile -n explain main.py

sudo mv dist/explain /usr/local/bin/explain

# and use it
explain docstring --file some.py
explain refactor --code 'for i in range(len(x)): print(x[i])' --model llama3
explain tests --file src/core/logic.py --description "don't focus on edge cases"
explain ask "how does recursion work?"
explain summarize src/api/routes.py
```

## notes

- ollama must be running

- assumes model behaves like a chat model (system/user messages)

- no context memory, it's stateless (maybe will change that in the future)

- not tested, just useful for quick work
