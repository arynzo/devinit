# DevInit 🚀

> **Node.js project scaffolding CLI** — ek command mein poora MVC structure ready.

```
  ██████╗ ███████╗██╗   ██╗██╗███╗   ██╗██╗████████╗
  ██╔══██╗██╔════╝██║   ██║██║████╗  ██║██║╚══██╔══╝
  ██║  ██║█████╗  ██║   ██║██║██╔██╗ ██║██║   ██║   
  ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║╚██╗██║██║   ██║   
  ██████╔╝███████╗ ╚████╔╝ ██║██║ ╚████║██║   ██║   
  ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   
```

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Table of Contents

1. [DevInit kya hai?](#1-devinit-kya-hai)
2. [Requirements](#2-requirements)
3. [Installation — Global Setup](#3-installation--global-setup)
4. [Usage — CLI Commands](#4-usage--cli-commands)
5. [--mvc Flag — Full Breakdown](#5---mvc-flag--full-breakdown)
6. [Terminal Output Example](#6-terminal-output-example)
7. [Project Structure (DevInit ka code)](#7-project-structure-devinit-ka-code)
8. [Naya Flag/Command Kaise Add Karein](#8-naya-flagcommand-kaise-add-karein)
9. [Uninstall](#9-uninstall)

---

## 1. DevInit kya hai?

**DevInit** ek Python-based CLI tool hai jo developers ko Node.js projects ke liye **professional folder structure aur boilerplate files** ek command mein generate kar deta hai.

Bina DevInit ke tumhe manually karna padta hai:

- Alag alag folders banana — `controllers/`, `models/`, `routes/` etc.
- `.env`, `.gitignore`, `index.js` likhna
- `package.json` mein scripts manually add karna
- Baar baar same setup repeat karna

**DevInit ke saath:**

```bash
devinit --mvc
```

...aur sab kuch ready. ✅

---

## 2. Requirements

DevInit ko chalane ke liye yeh installed hone chahiye:

| Requirement | Version | Check karo |
|---|---|---|
| Python | 3.8 ya usse upar | `python --version` |
| pip | Koi bhi recent | `pip --version` |

> **Node.js ki zarurat nahi** DevInit ko run karne ke liye. Node.js sirf tumhare generated project ke liye chahiye.

---

## 3. Installation — Global Setup

### Step 1 — ZIP extract karo

Download ke baad ZIP extract karo:

```bash
unzip devinit.zip
cd devinit
```

### Step 2 — Dependencies install karo

```bash
pip install -r requirements.txt
```

Yeh sirf ek package install karta hai: `colorama` (colored terminal output ke liye).

### Step 3 — CLI globally install karo

```bash
pip install -e .
```

Yeh `devinit` command tumhare system mein globally register kar deta hai. Ab tum **kisi bhi folder se** `devinit` run kar sakte ho.

### Step 4 — Verify karo

```bash
devinit --help
```

Agar yeh output aaye toh installation successful hai:

```
usage: devinit [-h] [--mvc]

DevInit — Node.js Project Scaffolding CLI

options:
  -h, --help  show this help message and exit
  --mvc       Scaffold a Node.js MVC folder structure with boilerplate files
```

---

## 4. Usage — CLI Commands

### Syntax

```bash
devinit [FLAG]
```

### Available Commands

| Command | Description |
|---|---|
| `devinit --mvc` | MVC folder structure + boilerplate files generate karo |
| `devinit --help` | Help message dekho |

### Agar koi flag na do

```bash
devinit
```

Output:

```
  ❌  Error: No command specified.
  Run  `devinit --help`  to see available commands.
```

DevInit bina flag ke nahi chalta — yeh intentional hai taaki galti se kuch na ho.

---

## 5. `--mvc` Flag — Full Breakdown

### Kaise use karein

Pehle apne Node.js project folder mein jao:

```bash
cd /path/to/your/project
devinit --mvc
```

> ⚠️ **DevInit current directory mein kaam karta hai.** Isliye pehle sahi folder mein jaana zaroori hai.

---

### Kya kya hota hai?

#### Folders banta hai (8 folders):

```
your-project/
├── config/          ← DB config, app config
├── controllers/     ← Route handlers / business logic
├── models/          ← Database models (Mongoose etc.)
├── routes/          ← Express route definitions
├── views/           ← Template files (EJS, Pug etc.)
├── middlewares/     ← Auth, logging, error middlewares
├── utils/           ← Helper functions
└── public/          ← Static files (CSS, JS, images)
```

#### Files create hoti hain:

**`.env`** — Environment variables ka template:

```env
NODE_ENV=development
PORT=3000
DB_URI=mongodb://localhost:27017/myapp
JWT_SECRET=your_jwt_secret_here
```

**`.gitignore`** — Node.js ke liye pre-configured:

```
node_modules/
.env
dist/
build/
logs/
*.log
.DS_Store
```

**`index.js`** — Basic Express starter:

```js
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
```

#### `package.json` update hota hai:

DevInit **existing `package.json` ko delete nahi karta** — sirf missing cheezein add karta hai:

- `"type": "module"` set hota hai (ES Modules support)
- `"scripts"` mein `"dev": "nodemon index.js"` add hota hai (agar pehle se nahi hai)
- `"scripts"` mein `"start": "node index.js"` add hota hai (agar pehle se nahi hai)
- Baaki saari existing fields safe rehti hain

**Agar `package.json` exist nahi karta**, toh DevInit ek minimal one khud bana deta hai.

---

### Safety Rules

| Situation | DevInit kya karta hai |
|---|---|
| Folder pehle se exist karta hai | Skip karta hai, warning dikhata hai |
| File pehle se exist karti hai | Skip karta hai, warning dikhata hai |
| `package.json` mein script pehle se hai | Overwrite nahi karta |
| Dobara `devinit --mvc` chalao | Kuch nahi toda, sirf warnings |

**DevInit is fully idempotent** — baar baar chalao, koi side effect nahi.

---

### Project ke baad kya karein

```bash
# Dependencies install karo
npm install express dotenv nodemon

# Development server chalao
npm run dev
```

---

## 6. Terminal Output Example

```
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
```

**Color coding:**
- 🟢 `✔` Green — successfully created
- 🟡 `⚠` Yellow — already exists, skipped
- 🔴 `❌` Red — error occurred
- 🔵 `ℹ` Cyan — info message

---

## 7. Project Structure (DevInit ka code)

```
devinit/
│
├── main.py                  ← CLI entry point
│                              Banner, argument parser, command registry
│
├── setup.py                 ← pip install ke liye config
│                              Global `devinit` command register hota hai yahan
│
├── requirements.txt         ← Python dependencies (sirf colorama)
│
├── README.md                ← Yahi file
│
├── commands/                ← Har ek CLI flag ka alag module
│   ├── __init__.py
│   └── mvc.py               ← --mvc command ka poora logic
│
└── utils/                   ← Shared utilities
    ├── __init__.py
    ├── file_ops.py          ← Safe file/folder operations, JSON read-write
    └── logger.py            ← Colored terminal output (success/warn/error/info)
```

---

## 8. Naya Flag/Command Kaise Add Karein

DevInit ki architecture is tarah banai gayi hai ki naya command add karna bahut aasaan hai — sirf 2 steps.

### Step 1 — Naya module banao

`commands/` folder mein naya file banao. Example: `commands/auth.py`

```python
# commands/auth.py

from utils.logger import header, info, done
from utils.file_ops import create_file

AUTH_MIDDLEWARE = """\
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
```

### Step 2 — `main.py` mein register karo

`main.py` kholo aur 2 jagah changes karo:

```python
# Top pe import karo
from commands import mvc, auth

# COMMANDS dict mein entry daalo
COMMANDS = {
    "mvc": {
        "handler": mvc.run,
        "help": "Scaffold a Node.js MVC folder structure",
        "flag": "--mvc",
    },
    "auth": {                           # ← yeh add karo
        "handler": auth.run,
        "help": "Scaffold JWT authentication boilerplate",
        "flag": "--auth",
    },
}
```

### Done ✅

```bash
devinit --auth
```

Koi aur wiring nahi, koi config nahi. CLI automatically new flag pick kar leta hai.

---

## 9. Uninstall

```bash
pip uninstall devinit
```

---

## License

MIT — freely use karein personal aur commercial projects mein.

---

> Build By Arynzo 🔥
