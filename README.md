# Running the project

## Windows
- Create the venv: `python -m venv venv`
- Navegate to the scripts venv directory: `cd venv/Scripts`
- `./activate`
- Install the dependencies: `pip install -r requirements.txt`
- Install the dev dependencies: `pip install -r requirements-dev.txt`
- Create the env variable: `$env:FLASK_ENV = "development"`
- Run: `flask run`

## Linux
- Create the venv: `python -m venv venv`
- Navegate to the scripts venv directory: `cd venv/bin`
- `./activate`
- Install the dependencies: `pip install -r requirements.txt`
- Install the dev dependencies: `pip install -r requirements-dev.txt`
- Run: `python run.py`

## Design Pattern
- Factories that avoid circular imports