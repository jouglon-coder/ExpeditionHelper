# Expedition Helper

A command-line helper for browsing and searching weapons and Pictos from **Clair Obscur: Expedition 33**.

## Features

* List all weapons
* List all Pictos
* Search weapons by effect
* Search weapons by element
* Filter weapons by owner
* Search Pictos by effect
* Search Pictos by location

## Installation

Python 3.10 or newer is required.

Clone the repository:

```bash
git clone https://github.com/jouglon-coder/ExpeditionHelper.git
cd ExpeditionHelper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

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
├── requirements.txt
└── README.md
```

## Project Status

The project is under development. Some data may be incomplete or inaccurate.

## Disclaimer

This is an unofficial, fan-made project created for personal and informational use.

Clair Obscur: Expedition 33, its characters, item names, weapon names, Pictos names, descriptions, terminology, and other game-related content are the property of their respective copyright and trademark owners.

This project is not affiliated with, endorsed by, sponsored by, or approved by Sandfall Interactive or Kepler Interactive.

The repository contains game-related data for reference and search purposes only. No ownership of the original game content is claimed.
