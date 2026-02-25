# GenAI

A small collection of GenAI experiments and demo scripts (QnA bots, agents, notebooks).

## Repo structure

- `apps/` — demo scripts and runnable examples
- `notebooks/` — exploration notebooks
- `env/` — local virtualenv (not committed)
- `requirements.txt` — Python dependencies

## Quickstart (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run an example (QnA bot):

```powershell
python apps\3_qna_bot_with_groq.py
```

## Notes

- This project uses a local virtual environment; see `.gitignore` for entries.
- Adjust Python version and dependency install as needed.

## License

This project is licensed under the MIT License — see `LICENSE`.
