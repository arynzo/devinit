"""
logger.py - Colored terminal output utility for DevInit
Uses colorama for cross-platform color support.
"""

from colorama import Fore, Style, init

# Auto-reset colors after each print
init(autoreset=True)


def success(msg: str):
    """Green checkmark for created files/folders."""
    print(f"{Fore.GREEN}  ✔  {msg}{Style.RESET_ALL}")


def warn(msg: str):
    """Yellow warning for already-existing resources."""
    print(f"{Fore.YELLOW}  ⚠  {msg}{Style.RESET_ALL}")


def error(msg: str):
    """Red cross for errors."""
    print(f"{Fore.RED}  ❌  {msg}{Style.RESET_ALL}")


def info(msg: str):
    """Cyan info line for general messages."""
    print(f"{Fore.CYAN}  ℹ  {msg}{Style.RESET_ALL}")


def header(msg: str):
    """Bold white section header."""
    print(f"\n{Style.BRIGHT}{Fore.WHITE}━━━  {msg}  ━━━{Style.RESET_ALL}\n")


def done(msg: str):
    """Bright green final success message."""
    print(f"\n{Style.BRIGHT}{Fore.GREEN}  🚀  {msg}{Style.RESET_ALL}\n")
