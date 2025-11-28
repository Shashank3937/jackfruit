# Flask Chatbot (Python 3.13 compatible)

This project is a minimal Flask chatbot that runs on Python 3.13.7.

It supports two modes:
- `rule`  : local rule-based chatbot (works without any external API).
- `openai`: forwards messages to OpenAI ChatCompletion (requires `openai` package and `OPENAI_API_KEY` env var).

## Files
- `app.py`       : Flask application
- `bot.py`       : ChatBot logic (rule-based + optional OpenAI)
- `templates/index.html` : Simple web UI
- `requirements.txt` : Python dependencies
- `README.md` : this file

## Quick start (rule-based, recommended for beginners)

1. Make sure you are using Python 3.13.7 (you mentioned this version).
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate    # Windows
   source venv/bin/activate   # macOS / Linux
   ```
3. Install Flask:
   ```
   pip install -r requirements.txt
   ```
   Note: `openai` is optional; install it only if you want OpenAI mode.
4. Run the app:
   ```
   python app.py
   ```
   Open your browser at `http://127.0.0.1:5000/`

## Using OpenAI mode (optional)

1. Install OpenAI package:
   ```
   pip install openai
   ```
2. Export your API key:
   - Windows (PowerShell):
     ```
     $env:OPENAI_API_KEY = "sk-..."
     ```
   - Windows (cmd.exe):
     ```
     set OPENAI_API_KEY=sk-...
     ```
   - macOS / Linux:
     ```
     export OPENAI_API_KEY="sk-..."
     ```
3. In `app.py`, create the bot with `ChatBot(mode='openai')` instead of `mode='rule'`.

## Notes
- This project avoids ChatterBot and therefore works on modern Python versions including 3.13.
- The rule-based bot is intentionally simple so you can study and extend it.
- If you want, I can help add persistence, better NLP, or deploy the app online.
