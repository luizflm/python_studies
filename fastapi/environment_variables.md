# Environment Variables
An environment variable (also known as "env var") is a variable that lives outside of the Python code, in the operating system, and could be read by your Python code (or by other programs as well).

Environment variables could be useful for handling application settings, as part of the installation of Python, etc.

## Creating Env Vars
You can create and use environment variables in the shell (terminal), without needing Python:
```bash
# You could create an env var MY_NAME with
export MY_NAME="Wade Wilson"
```

## Read env vars in Python
You could also create environment variables outside of Python, in the terminal (or with any other method), and then read them in Python.

For example you could have a file main.py with:
```python
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
```

As environment variables can be set outside of the code, but can be read by the code, and don't have to be stored (committed to git) with the rest of the files, it's common to use them for configurations or settings.

You can also create an environment variable only for a specific program invocation, that is only available to that program, and only for its duration.

To do that, create it right before the program itself, on the same line:
```bash
# Create an env var MY_NAME in line for this program call
MY_NAME="Wade Wilson" python main.py
```