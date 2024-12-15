import os
from dotenv import load_dotenv

load_dotenv()

CHATGPT_API_KEY = os.getenv("OPENAI_API_KEY")
GAME_URL = "https://neal.fun/password-game/"
