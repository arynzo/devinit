# DevInit 🚀

> Node.js project scaffolding CLI — complete MVC structure ready with a single command.

  ██████╗ ███████╗██╗   ██╗██╗███╗   ██╗██╗████████╗
  ██╔══██╗██╔════╝██║   ██║██║████╗  ██║██║╚══██╔══╝
  ██║  ██║█████╗  ██║   ██║██║██╔██╗ ██║██║   ██║   
  ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║╚██╗██║██║   ██║   
  ██████╔╝███████╗ ╚████╔╝ ██║██║ ╚████║██║   ██║   
  ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   

Python 3.8+ | License: MIT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TABLE OF CONTENTS

  1. What is DevInit?
  2. Requirements
  3. Installation — Global Setup
  4. Usage — CLI Commands
  5. --mvc Flag — Full Breakdown
  6. Terminal Output Example
  7. Project Structure (DevInit's own code)
  8. How to Add a New Flag / Command
  9. Uninstall

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. WHAT IS DEVINIT?

DevInit is a Python-based CLI tool that generates a professional Node.js folder
structure and boilerplate files with a single command.

Without DevInit, you have to manually:
  - Create folders one by one — controllers/, models/, routes/, etc.
  - Write .env, .gitignore, and index.js from scratch
  - Manually add scripts to package.json
  - Repeat the same boring setup for every new project

With DevInit:

  devinit --mvc

...and everything is ready.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2. REQUIREMENTS

The following must be installed on your system:

  Requirement   Version          How to check
  ─────────────────────────────────────────────
  Python        3.8 or above     python --version
  pip           Any recent       pip --version

NOTE: Node.js is NOT required to run DevInit itself.
Node.js is only needed for the project you generate.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. INSTALLATION — GLOBAL SETUP

Step 1 — Extract the ZIP

  unzip devinit.zip
  cd devinit

Step 2 — Install dependencies

  pip install -r requirements.txt

This installs one package: colorama (for colored terminal output).

Step 3 — Install the CLI globally

  pip install -e .

This registers the devinit command system-wide.
After this, you can run devinit from ANY folder on your system.

Step 4 — Verify the installation

  devinit --help

If you see this, installation was successful:

  usage: devinit [-h] [--mvc]

  DevInit — Node.js Project Scaffolding CLI

  options:
    -h, --help  show this help message and exit
    --mvc       Scaffold a Node.js MVC folder structure with boilerplate files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4. USAGE — CLI COMMANDS

Syntax:
  devinit [FLAG]

Available commands:

  Command              Description
  ─────────────────────────────────────────────────────────────────
  devinit --mvc        Generate MVC folder structure + boilerplate
  devinit --help       Show help message

If you run devinit without any flag:

  devinit

Output:
  ❌  Error: No command specified.
  Run `devinit --help` to see available commands.

This is intentional — DevInit will never run accidentally.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. --mvc FLAG — FULL BREAKDOWN

How to use it:

First, navigate to your Node.js project folder:

  cd /path/to/your/project
  devinit --mvc

IMPORTANT: DevInit operates in the CURRENT directory.
Make sure you are inside the right folder before running.

─────────────────────────────────────────────────────

WHAT GETS CREATED:

Folders (8 total):

  your-project/
  ├── config/          ← DB config, app config
  ├── controllers/     ← Route handlers / business logic
  ├── models/          ← Database models (Mongoose etc.)
  ├── routes/          ← Express route definitions
  ├── views/           ← Template files (EJS, Pug etc.)
  ├── middlewares/     ← Auth, logging, error middlewares
  ├── utils/           ← Helper/utility functions
  └── public/          ← Static files (CSS, JS, images)

─────────────────────────────────────────────────────

Files:

.env — Environment variable template:

  NODE_ENV=development
  PORT=3000
  DB_URI=mongodb://localhost:27017/myapp
  JWT_SECRET=your_jwt_secret_here

.gitignore — Pre-configured for Node.js:

  node_modules/
  .env
  dist/
  build/
  logs/
  *.log
  .DS_Store

index.js — Basic Express starter:

  import express from 'express';
  import dotenv from 'dotenv';

  dotenv.config();

  const app = express();
  const PORT = process.env.PORT || 3000;

  app.use(express.json());

  app.get('/', (req, res) => {
    res.json({ message: 'Server is running 🚀', status: 'ok' });
  });

  app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });

─────────────────────────────────────────────────────

package.json update:

DevInit does NOT delete your existing package.json.
It only adds what is missing:

  - Sets "type": "module"  (ES Modules support)
  - Adds "dev": "nodemon index.js"  to scripts (if not already there)
  - Adds "start": "node index.js"   to scripts (if not already there)
  - All your existing fields are kept safe

If no package.json exists, DevInit creates a minimal one.

─────────────────────────────────────────────────────

SAFETY RULES:

  Situation                              DevInit behavior
  ──────────────────────────────────────────────────────────────
  Folder already exists                  Skips it, shows warning
  File already exists                    Skips it, shows warning
  Script already in package.json         Does not overwrite it
  Run devinit --mvc a second time        Nothing breaks, warnings only

DevInit is fully idempotent — safe to run multiple times.

─────────────────────────────────────────────────────

AFTER SCAFFOLDING — next steps:

  npm install express dotenv nodemon
  npm run dev

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6. TERMINAL OUTPUT EXAMPLE

  ━━━  DevInit  →  MVC Scaffold  ━━━

    ℹ  Scaffolding MVC structure in current directory...

  ━━━  Creating Folders  ━━━

    ✔  Created folder:  config/
    ✔  Created folder:  controllers/
    ✔  Created folder:  models/
    ✔  Created folder:  routes/
    ✔  Created folder:  views/
    ✔  Created folder:  middlewares/
    ✔  Created folder:  utils/
    ✔  Created folder:  public/

  ━━━  Creating Files  ━━━

    ✔  Created file:    .env
    ✔  Created file:    .gitignore
    ✔  Created file:    index.js

  ━━━  Updating package.json  ━━━

    ✔  Updated file:    package.json

    🚀  MVC scaffold complete! Run `npm install` to get started.

Color coding:
  ✔  Green   — successfully created
  ⚠  Yellow  — already exists, skipped
  ❌  Red     — error occurred
  ℹ  Cyan    — info message

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7. PROJECT STRUCTURE (DEVINIT'S OWN CODE)

  devinit/
  │
  ├── setup.py                   ← pip install config
  │                                Registers the global devinit command
  │
  ├── requirements.txt           ← Python dependencies (colorama only)
  │
  ├── README.txt                 ← This file
  │
  └── devinit_cli/               ← Main Python package
      ├── __init__.py
      ├── __main__.py            ← CLI entry point, banner, arg parser, command registry
      │
      ├── commands/              ← One file per CLI flag
      │   ├── __init__.py
      │   └── mvc.py             ← All logic for --mvc
      │
      └── utils/                 ← Shared utilities
          ├── __init__.py
          ├── file_ops.py        ← Safe file/folder creation, JSON read-write
          └── logger.py          ← Colored terminal output helpers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8. HOW TO ADD A NEW FLAG / COMMAND

DevInit's architecture makes adding new commands very easy — just 2 steps.

─────────────────────────────────────────────────────

Step 1 — Create a new module in commands/

Example: commands/auth.py

  # commands/auth.py

  from devinit_cli.utils.logger import header, info, done
  from devinit_cli.utils.file_ops import create_file

  AUTH_MIDDLEWARE = """
  // middlewares/auth.js
  import jwt from 'jsonwebtoken';

  export const protect = (req, res, next) => {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) return res.status(401).json({ error: 'Not authorized' });
    try {
      req.user = jwt.verify(token, process.env.JWT_SECRET);
      next();
    } catch {
      res.status(401).json({ error: 'Invalid token' });
    }
  };
  """

  def run():
      header("DevInit  →  Auth Scaffold")
      info("Setting up JWT auth boilerplate...\n")
      create_file("middlewares/auth.js", AUTH_MIDDLEWARE)
      done("Auth scaffold complete!")

─────────────────────────────────────────────────────

Step 2 — Register it in devinit_cli/__main__.py

  # Add the import at the top
  from devinit_cli.commands import mvc, auth

  # Add an entry to the COMMANDS dict
  COMMANDS = {
      "mvc": {
          "handler": mvc.run,
          "help": "Scaffold a Node.js MVC folder structure",
          "flag": "--mvc",
      },
      "auth": {                            # <-- add this
          "handler": auth.run,
          "help": "Scaffold JWT authentication boilerplate",
          "flag": "--auth",
      },
  }

─────────────────────────────────────────────────────

That's it. Run:

  devinit --auth

No other wiring needed. The CLI picks up the new flag automatically.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

9. UNINSTALL

  pip uninstall devinit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LICENSE

MIT — free to use in personal and commercial projects.

Built with Python + colorama
