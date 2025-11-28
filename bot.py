import os
import random

# Optional OpenAI integration. It only runs if mode='openai' and OPENAI_API_KEY env var exists.
try:
    import openai
except Exception:
    openai = None

class ChatBot:
    def __init__(self, mode='rule'):
        # mode: 'rule' for local simple bot, 'openai' to forward to OpenAI API (if available)
        self.mode = mode
        # simple rule-based patterns (very basic)
        self.rules = {
            'hello': ['Hi there!', 'Hello!', 'Hey! How can I help you?'],
            'hi': ['Hello!', 'Hi!'],
            'how are you': ["I'm a bot, but I'm working fine 🙂", "Doing great! How about you?"],
            'what is your name': ['I am your assistant chatbot.', 'You can call me ChatBot.'],
            'help': ['I can answer simple questions. Try: "What is your name?", "How are you?", or ask me to calculate like: calc 2+3'],
        }

    def get_response(self, message: str) -> str:
        message = (message or "").strip()
        if not message:
            return "Please type something."

        # basic calculator support: if message starts with "calc " evaluate safely
        if message.lower().startswith("calc "):
            expr = message[5:].strip()
            try:
                # Safe eval: allow digits, operators, parentheses, decimal point, spaces
                allowed = set("0123456789+-*/(). %")
                if any(ch not in allowed for ch in expr):
                    return "Calculator only supports digits and + - * / ( ) ."
                # evaluate
                result = eval(expr, {"__builtins__": None}, {})
                return f"Result: {result}"
            except Exception:
                return "Couldn't evaluate that expression."

        # If mode openai and openai package + key available, forward to OpenAI
        if self.mode == 'openai':
            api_key = os.getenv('OPENAI_API_KEY')
            if openai is None or not api_key:
                return "OpenAI mode requested but OpenAI package or API key is missing. Set OPENAI_API_KEY or use mode='rule'."
            try:
                openai.api_key = api_key
                # Use a lightweight chat completion (user can change model)
                completion = openai.ChatCompletion.create(
                    model="gpt-4o-mini",  # example model name; user can adjust
                    messages=[{"role":"user","content": message}],
                    max_tokens=256,
                    temperature=0.7
                )
                resp = completion.choices[0].message.content.strip()
                return resp
            except Exception as e:
                return f"OpenAI error: {e}"

        # Rule-based matching (simple)
        low = message.lower()
        # exact triggers
        for key in self.rules:
            if key in low:
                return random.choice(self.rules[key])

        # fallback small canned responses based on keywords
        if any(word in low for word in ["time", "date"]):
            from datetime import datetime
            return datetime.now().strftime("Current date/time: %Y-%m-%d %H:%M:%S")
        if "name" in low:
            return "You can call me ChatBot."
        if "thanks" in low or "thank you" in low:
            return "You're welcome!"
        if "bye" in low or "goodbye" in low:
            return "Goodbye! Have a great day."

        # default
        return "Sorry, I didn't understand that. Try asking something else, or type 'help'."
