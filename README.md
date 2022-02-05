# Projet 4 : Développez un programme logiciel en Python

This Python program allow to manage chess tournament.

## Getting Started

### Create the virtual environment

1. Go to the project folder via the terminal.
Create the virtual environment using the command :

 ```bash
python -m venv <environment_name>
```

2. Activate using the virtual enviroment:

- on Linux :

```bash
source <environment_name>/bin/activate
```

- on Windows:

```bash
<environment_name>/Scripts/activate.bat
```

### Dependencies

Install packages from requirements.txt using

```bash
 pip install -r requirements.txt
 ```

### Executing program

Run main.py to execute:

 ```bash
 python code/main.py
 ```

> :warning: **Be sure to only use your keyboard while using the program.**

### Generate a new flake8 report
Delete the contents of the folder flake8_rapport, then run:
```bash
flake8 --max-line-length 119 code --format=html --htmldir=flake8_rapport
```