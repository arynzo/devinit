"""
mvc.py - Scaffolds a clean MVC folder structure for Node.js projects.
Triggered by: devinit --mvc
"""

from devinit_cli.utils.file_ops import create_folder, create_file, read_json, write_json
from devinit_cli.utils.logger import header, info, done

# ──────────────────────────────────────────────
# Folder structure to scaffold
# ──────────────────────────────────────────────
MVC_FOLDERS = [
    "config",
    "controllers",
    "models",
    "routes",
    "views",
    "middlewares",
    "utils",
    "public",
]

# ──────────────────────────────────────────────
# File templates
# ──────────────────────────────────────────────
ENV_CONTENT = """\
# Environment Variables
NODE_ENV=development
PORT=3000

# Database
DB_URI=mongodb://localhost:27017/myapp

# JWT
JWT_SECRET=your_jwt_secret_here
"""

GITIGNORE_CONTENT = """\
# Dependencies
node_modules/

# Environment
.env

# Build output
dist/
build/

# Logs
logs/
*.log
npm-debug.log*

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
"""

INDEX_JS_CONTENT = """\
// index.js - Entry point
import express from 'express';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'Server is running 🚀', status: 'ok' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
"""


def run():
    """Entry point for the --mvc command."""

    header("DevInit  →  MVC Scaffold")
    info("Scaffolding MVC structure in current directory...\n")

    # 1. Create folders
    header("Creating Folders")
    for folder in MVC_FOLDERS:
        create_folder(folder)

    # 2. Create static files
    header("Creating Files")
    create_file(".env", ENV_CONTENT)
    create_file(".gitignore", GITIGNORE_CONTENT)
    create_file("index.js", INDEX_JS_CONTENT)

    # 3. Update package.json (non-destructive merge)
    header("Updating package.json")
    _update_package_json()

    done("MVC scaffold complete! Run  `npm install`  to get started.")


def _update_package_json():
    """
    Reads existing package.json and merges in required fields.
    Does NOT overwrite any existing content — only adds missing keys.
    """
    pkg = read_json("package.json")

    if not pkg:
        info("No package.json found — creating a minimal one.")
        pkg = {
            "name": "my-app",
            "version": "1.0.0",
            "description": "",
            "main": "index.js",
        }

    # Set ESM module type
    pkg["type"] = "module"

    # Merge scripts without overwriting user's existing scripts
    existing_scripts = pkg.get("scripts", {})
    if "dev" not in existing_scripts:
        existing_scripts["dev"] = "nodemon index.js"
    if "start" not in existing_scripts:
        existing_scripts["start"] = "node index.js"
    pkg["scripts"] = existing_scripts

    write_json("package.json", pkg)
