#!/usr/bin/env python3
"""
DevInit - Developer Project Scaffolding CLI
==========================================
Quickly scaffold and bootstrap Node.js project structures
from the terminal with a single command.

Usage:
    devinit --mvc
    devinit --express-boiler

Author: DevInit CLI
"""

import argparse
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# ──────────────────────────────────────────────
# ASCII Banner
# ──────────────────────────────────────────────
BANNER = f"""
{Fore.CYAN}{Style.BRIGHT}
  ██████╗ ███████╗██╗   ██╗██╗███╗   ██╗██╗████████╗
  ██╔══██╗██╔════╝██║   ██║██║████╗  ██║██║╚══██╔══╝
  ██║  ██║█████╗  ██║   ██║██║██╔██╗ ██║██║   ██║   
  ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║╚██╗██║██║   ██║   
  ██████╔╝███████╗ ╚████╔╝ ██║██║ ╚████║██║   ██║   
  ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   
{Style.RESET_ALL}
{Fore.WHITE}  Node.js Project Scaffolding CLI  •  v1.0.0{Style.RESET_ALL}
  {Fore.YELLOW}──────────────────────────────────────────{Style.RESET_ALL}
"""


# ──────────────────────────────────────────────
# Command Registry
# ──────────────────────────────────────────────
# To add a new command:
#   1. Create commands/yourcommand.py with a run() function
#   2. Import it below
#   3. Add an entry to COMMANDS dict with flag + metadata
#
# That's it. The CLI wiring is fully automatic.

from devinit_cli.commands import mvc

COMMANDS = {
    "mvc": {
        "handler": mvc.run,
        "help": "Scaffold a Node.js MVC folder structure with boilerplate files",
        "flag": "--mvc",
    },
    # ── Add new commands here ──────────────────
    # "auth": {
    #     "handler": auth.run,
    #     "help": "Scaffold JWT authentication boilerplate",
    #     "flag": "--auth",
    # },
    # "ts": {
    #     "handler": typescript.run,
    #     "help": "Add TypeScript configuration to the project",
    #     "flag": "--ts",
    # },
}


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="devinit",
        description="DevInit — Node.js Project Scaffolding CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=_build_epilog(),
        add_help=True,
    )

    # Register all commands as mutually exclusive flags
    group = parser.add_mutually_exclusive_group()

    for key, meta in COMMANDS.items():
        flag = meta["flag"]
        dest = key  # argparse dest key
        group.add_argument(
            flag,
            dest=dest,
            action="store_true",
            default=False,
            help=meta["help"],
        )

    return parser


def _build_epilog() -> str:
    """Generate usage examples for the help footer."""
    lines = [
        "",
        "Examples:",
    ]
    for meta in COMMANDS.values():
        lines.append(f"  devinit {meta['flag']:<20}  {meta['help']}")
    lines.append("")
    lines.append("Run 'devinit --help' to see all available commands.")
    return "\n".join(lines)


def main():
    print(BANNER)

    parser = build_parser()
    args = parser.parse_args()

    # Check if at least one flag was passed
    args_dict = vars(args)
    selected = [key for key, val in args_dict.items() if val is True]

    if not selected:
        print(f"{Fore.RED}{Style.BRIGHT}  ❌  Error: No command specified.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}  Run  `devinit --help`  to see available commands.{Style.RESET_ALL}\n")
        sys.exit(1)

    # Execute the matching command handler
    command_key = selected[0]
    handler = COMMANDS[command_key]["handler"]
    handler()


if __name__ == "__main__":
    main()
