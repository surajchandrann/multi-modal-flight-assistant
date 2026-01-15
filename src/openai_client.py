import openai
import base64
from io import BytesIO
from PIL import Image
from src.config import OPENAI_API_KEY,MODEL,IMAGE_MODEL,IMAGE_SIZE,TTS_MODEL,TTS_VOICE

client = openai.OpenAI(api_key=OPENAI_API_KEY)
def generate_image(city):
    response = client.images.generate(
        model=IMAGE_MODEL,
        prompt=f"Vacation in {city}, tourist spots, vibrant pop-art style",
        size=IMAGE_SIZE, n=1, response_format="b64_json"
    )
    image_data = base64.b64decode(response.data[0].b64_json)
    return Image.open(BytesIO(image_data))

def text_to_speech(text):
    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text
    )
    return response.content