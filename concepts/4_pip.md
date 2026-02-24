# Pip
"Pip" stands for "Pip Installs Packages". It's Python's official package manager that lets you install and manage third-party libraries and tools.

## Installing packages
```bash
pip install requests
```

## Uninstalling packages
```bash
pip uninstall requests
```

## Listing packages
```bash
pip list
```

## Show package info
```bash
pip show requests
```

## Upgrading packages
```bash
pip install --upgrade requests
# or
pip install -U requests
```

## Freezing dependencies
```bash
# Generate requirements.txt with all installed packages
pip freeze > requirements.txt
```

# Virtual Environments
Virtual environments isolate project dependencies. Each project gets its own package versions without conflicts.

## Why use virtual environments?
- Project A needs Django 3.2
- Project B needs Django 4.2
- Without virtual environments, you can have conflits.
- With virtual environments, both projects will work perfectly.

## Creating Virtual Environments

**Using venv (built-in):**
```bash
python -m venv myenv

# Or with specific name
python -m venv venv
python -m venv .venv
```

## Activating Virtual Environments

**Windows:**
```bash
# Command Prompt
myenv\Scripts\activate.bat

# PowerShell
myenv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source myenv/bin/activate
```

**After activation, your prompt changes:**
```bash
(myenv) user@computer:~/project$
```

### Deactivating
```bash
deactivate
```