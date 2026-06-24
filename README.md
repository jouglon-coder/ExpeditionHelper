# Expedition Helper

A command-line helper for searching weapons and Pictos from **Clair Obscur: Expedition 33**.

## Features

* List all weapons and Pictos
* Search weapons by effect
* Search weapons by element and owner
* Search Pictos by effect
* Search Pictos by location

## Installation

Python 3.10 or newer is required.

```bash
git clone https://github.com/jouglon-coder/ExpeditionHelper.git
cd ExpeditionHelper

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```

## Usage

```bash
python main.py
```

Follow the prompts shown in the terminal.

When filtering weapons by owner, enter one of the following:

```text
Verso
Lune
Maelle
Sciel
Monoco
any
```

Use `any` to search weapons belonging to all characters.

## Project Structure

```text
ExpeditionHelper/
├── data/
│   ├── pictos.py
│   └── weapons.py
├── main.py
├── manager.py
├── models.py
└── requirements.txt
```

## Project Status

The project is under development. Some data may be incomplete or inaccurate.
