"""Safe subprocess adapter to a separately installed CMMRLab/LUNAR checkout.

LUNAR owns its CLI syntax. This adapter does not pretend to parameterize atoms,
and never substitutes guessed PCFF coefficients.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys

TOOLS = ("atom_typing", "all2lmp", "bond_react_merge_prep", "bond_react_merge")

def locate(root: Path, tool: str) -> Path:
    if tool not in TOOLS:
        raise ValueError(f"Unsupported LUNAR tool: {tool}")
    script = root.expanduser().resolve() / f"{tool}.py"
    if not script.is_file():
        raise FileNotFoundError(f"Missing {script}; clone CMMRLab/LUNAR first")
    return script

def invoke(root: Path, tool: str, arguments: list[str], *, timeout: int = 3600,
           execute: bool = False, log: Path | None = None) -> int:
    script = locate(root, tool)
    if not arguments:
        raise ValueError("Provide explicit LUNAR options (e.g. -man); defaults may launch unwanted jobs")
    if arguments == ["-man"] or arguments == ["-opt"]:
        execute = True  # safe help mode
    cmd = [sys.executable, str(script), *arguments]
    print("Command:", " ".join(cmd), flush=True)
    if not execute:
        print("DRY RUN: add --execute after reviewing LUNAR -man and your parameter source.")
        return 0
    result = subprocess.run(cmd, cwd=str(script.parent), capture_output=True,
                            text=True, timeout=timeout, check=False)
    if log is not None:
        log.parent.mkdir(parents=True, exist_ok=True)
        log.write_text(result.stdout + "\n--- STDERR ---\n" + result.stderr, encoding="utf-8")
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode:
        raise RuntimeError(f"LUNAR {tool} failed with return code {result.returncode}")
    return result.returncode

def main() -> None:
    parser = argparse.ArgumentParser(description="LUNAR adapter: preview command by default")
    parser.add_argument("--root", type=Path, required=True, help="CMMRLab/LUNAR source directory")
    parser.add_argument("--tool", choices=TOOLS, required=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--log", type=Path)
    parser.add_argument("--timeout", type=int, default=3600)
    parser.add_argument("lunar_options", nargs=argparse.REMAINDER,
                        help="Pass options after --, e.g. -- -man")
    args = parser.parse_args()
    opts = args.lunar_options
    if opts and opts[0] == "--":
        opts = opts[1:]
    invoke(args.root, args.tool, opts, timeout=args.timeout, execute=args.execute, log=args.log)

if __name__ == "__main__":
    main()
