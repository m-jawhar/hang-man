# Hangman (C and Python)

This repo holds two Hangman implementations side by side:

- `c/` – C version
- `python/` – Python version

## C version (in `c/`)

Build and run with GCC:

```bash
gcc hangman.c -o hangman
./hangman
```

On Windows PowerShell:

```powershell
gcc hangman.c -o hangman
./hangman
```

## Python version (in `python/`)

A complete, object-oriented Python implementation with scoring, statistics tracking, and a clean command-line interface.

Run the game:

```bash
python python/hangman.py
```

Or navigate into the folder:

```bash
cd python
python hangman.py
```

See [python/README.md](./python/README.md) for full details.

## Repo notes

- Kept language-specific files in their folders.
- Added per-language docs (e.g., `c/README.md`, `python/README.md`) if needed.
