"""
file_ops.py - Safe file and folder operations for DevInit
All operations check for existing resources before acting.
"""

import os
import json
from devinit_cli.utils.logger import success, warn, error


def create_folder(path: str) -> bool:
    """
    Create a folder at the given path (relative to cwd).
    Skips silently if folder already exists.
    Returns True if created, False if already existed.
    """
    abs_path = os.path.join(os.getcwd(), path)
    if os.path.exists(abs_path):
        warn(f"Folder already exists: {path}/")
        return False
    try:
        os.makedirs(abs_path)
        success(f"Created folder:  {path}/")
        return True
    except Exception as e:
        error(f"Could not create folder '{path}': {e}")
        return False


def create_file(path: str, content: str = "") -> bool:
    """
    Create a file at the given path (relative to cwd).
    Skips silently if file already exists.
    Returns True if created, False if already existed.
    """
    abs_path = os.path.join(os.getcwd(), path)
    if os.path.exists(abs_path):
        warn(f"File already exists:   {path}")
        return False
    try:
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        success(f"Created file:    {path}")
        return True
    except Exception as e:
        error(f"Could not create file '{path}': {e}")
        return False


def overwrite_file(path: str, content: str) -> bool:
    """
    Force-write a file (used when we intentionally want to update).
    """
    abs_path = os.path.join(os.getcwd(), path)
    try:
        os.makedirs(os.path.dirname(abs_path) or ".", exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        success(f"Updated file:    {path}")
        return True
    except Exception as e:
        error(f"Could not write file '{path}': {e}")
        return False


def read_json(path: str) -> dict:
    """
    Read and parse a JSON file from cwd.
    Returns empty dict if file doesn't exist or is invalid.
    """
    abs_path = os.path.join(os.getcwd(), path)
    if not os.path.exists(abs_path):
        return {}
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        error(f"Invalid JSON in '{path}'. Skipping update.")
        return {}


def write_json(path: str, data: dict) -> bool:
    """
    Write a dict as pretty-printed JSON to the given path.
    """
    abs_path = os.path.join(os.getcwd(), path)
    try:
        with open(abs_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        success(f"Updated file:    {path}")
        return True
    except Exception as e:
        error(f"Could not write JSON '{path}': {e}")
        return False
