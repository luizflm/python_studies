# Modules
A module is simply a Python file (.py) that contains Python code - functions, classes, variables.
```python
import functions
import config
```

## Why Use Modules?

1. **Code Organization** - Keep related code together
2. **Reusability** - Use the same code across multiple files
3. **Namespace Management** - Avoid naming conflicts
4. **Maintainability** - Easier to update and debug

## Types of Modules

### 1. Built-in Modules (Standard Library)
Python comes with many pre-installed modules:
- `os` - Operating system operations
- `sys` - System-specific parameters
- `math` - Mathematical functions
- `datetime` - Date and time handling
- `random` - Random number generation
- `json` - JSON encoding/decoding
- `re` - Regular expressions

### 2. Third-Party Modules
Installed via pip (Python's package manager):
- `requests` - HTTP requests
- `pandas` - Data analysis
- `flask` - Web framework
- `numpy` - Numerical computing

### 3. Your Own Modules
Any `.py` file you create becomes a module!

## Import Statements - All Methods

### 1. Basic Import
```python
import math

# Use with module name prefix
result = math.sqrt(16)
pi = math.pi
print(result)  # 4.0
print(pi)      # 3.141592653589793
```

### 2. Import with Alias
```python
import math as m

result = m.sqrt(16)
pi = m.pi
```

**Use case:** Shorter names for frequently used modules
```python
import numpy as np
import pandas as pd
```

### 3. Import Specific Items
```python
from math import sqrt, pi

# Use directly without prefix
result = sqrt(16)
print(pi)
```

### 4. Import Everything (Not Recommended)
```python
from math import *

# All functions available directly
result = sqrt(16)
print(pi)
print(cos(0))
```

### 5. Import Specific Items with Alias
```python
from math import sqrt as square_root

result = square_root(16)
```

### 6. Import Multiple Items
```python
from math import sqrt, pi, cos, sin

# Or with line breaks for readability
from math import (
    sqrt,
    pi,
    cos,
    sin,
    tan
)
```

## Module Search Path

When you import a module, Python searches in this order:

1. **Current directory** (where your script is)
2. **PYTHONPATH** environment variable directories
3. **Standard library** directories
4. **Site-packages** (where pip installs packages)

## Packages (Modules with Subdirectories)

A **package** is a directory containing modules and a special `__init__.py` file.

## Common Built-in Modules Examples

### 1. `os` - Operating System Operations
```python
import os

# Get current directory
current_dir = os.getcwd()
print(current_dir)

# List files in directory
files = os.listdir('.')
print(files)

# Check if file exists
exists = os.path.exists('myfile.txt')

# Create directory
os.makedirs('new_folder', exist_ok=True)

# Join paths (works on all OS)
path = os.path.join('folder', 'subfolder', 'file.txt')

# Get file size
size = os.path.getsize('myfile.txt')
```

### 2. `sys` - System-Specific Parameters
```python
import sys

# Command line arguments
print(sys.argv)  # ['script.py', 'arg1', 'arg2']

# Exit program
sys.exit(0)

# Python version
print(sys.version)

# Add to module search path
sys.path.append('/custom/path')
```

### 3. `datetime` - Date and Time
```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)

# Current date only
today = date.today()
print(today)

# Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# Parse string to date
date_obj = datetime.strptime("2026-01-30", "%Y-%m-%d")

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

### 4. `json` - JSON Encoding/Decoding
```python
import json

# Python dict to JSON string
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

# Pretty print
pretty_json = json.dumps(data, indent=4)
print(pretty_json)

# JSON string to Python dict
parsed = json.loads(json_string)
print(parsed["name"])

# Read from file
with open('data.json', 'r') as f:
    data = json.load(f)

# Write to file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### 5. `random` - Random Number Generation
```python
import random

# Random float between 0 and 1
print(random.random())

# Random integer between a and b (inclusive)
print(random.randint(1, 100))

# Random choice from list
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

# Shuffle list in place
random.shuffle(fruits)

# Random sample (multiple items)
print(random.sample(fruits, 2))
```

### 6. `re` - Regular Expressions
```python
import re

text = "My email is john@example.com and phone is 123-456-7890"

# Find email
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
if email:
    print(email.group())  # john@example.com

# Find all numbers
numbers = re.findall(r'\d+', text)
print(numbers)  # ['123', '456', '7890']

# Replace
new_text = re.sub(r'\d', 'X', text)
print(new_text)  # My email is john@example.com and phone is XXX-XXX-XXXX

# Split by pattern
parts = re.split(r'[,.]', "a,b.c,d")
print(parts)  # ['a', 'b', 'c', 'd']
```

### 7. `pathlib` - Object-Oriented File Paths
```python
from pathlib import Path

# Current directory
current = Path.cwd()

# Join paths
path = Path('folder') / 'subfolder' / 'file.txt'

# Check if exists
if path.exists():
    print("File exists")

# Read file
content = path.read_text()

# Write file
path.write_text("Hello, World!")

# Get file info
print(path.name)        # file.txt
print(path.stem)        # file
print(path.suffix)      # .txt
print(path.parent)      # folder/subfolder

# List directory
for item in Path('.').iterdir():
    print(item)

# Find all .py files recursively
for py_file in Path('.').rglob('*.py'):
    print(py_file)
```

## Installing Third-Party Modules with pip

### Install a package
```bash
pip install requests
pip install flask
pip install pandas
```

### Install specific version
```bash
pip install requests==2.28.0
```

### Install from requirements file
```bash
pip install -r requirements.txt
```

### Create requirements.txt
```bash
pip freeze > requirements.txt
```

### Uninstall package
```bash
pip uninstall requests
```

### List installed packages
```bash
pip list
```

## The `__name__` and `__main__` Pattern

This is crucial for creating modules that can be both imported and run directly.

**File: `mymodule.py`**
```python
def my_function():
    return "Hello from my_function"

# This code only runs when file is executed directly
if __name__ == "__main__":
    print("This is the main program")
    result = my_function()
    print(result)
    
    # Run tests
    print("Running tests...")
    assert my_function() == "Hello from my_function"
    print("All tests passed!")
```

**When you run:** `python mymodule.py`
- Output: "This is the main program", "Hello from my_function", etc.

**When you import:** `import mymodule`
- The `if __name__ == "__main__"` block does NOT run
- Only the function definition is available

This pattern lets you:
1. Write reusable modules
2. Include test code that doesn't run on import
3. Create command-line tools that can also be imported
