from openai import OpenAI
from config import OPENAI_API_KEY
import requests, os

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image(prompt, index):
    img = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1792"
    )

    url = img.data[0].url
    os.makedirs("output/images", exist_ok=True)
    path = f"output/images/scene_{index}.png"

    with open(path, "wb") as f:
        f.write(requests.get(url).content)

    return path
