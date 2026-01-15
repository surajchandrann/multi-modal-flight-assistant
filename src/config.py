import os
from dotenv import load_dotenv

load_dotenv()

# Api Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('MODEL',"gpt-4o-mini")

# Database
DB_PATH = os.getenv('DB_PATH', "prices.db")

# Image Generation
IMAGE_MODEL = os.getenv('IMAGE_MODEL', "dall-e-3")
IMAGE_SIZE = os.getenv('IMAGE_SIZE',"1024x1024")

# TTS
TTS_MODEL = os.getenv('TTS_MODEL',"tts-1")
TTS_VOICE = os.getenv("TTS_VOICE","onyx")

SYSTEM_MESSAGE =  """
You are FlightAI assistant. Short, courteous 1-sentence answers only.
"""