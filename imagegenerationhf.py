import requests
from PIL import images
from io import BytesIO
from config import hf_api_key
 
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
def generate_image_from_text(prompt : str)-> Image.Image():
    """Sent a text prompt to hugging face and get generated image"""
    headers = {"Authorization" : f"Bearer" {hf_api_key}}
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=headers , json=payload, time=30)
        response.raise_for_status()

        if "image" in requests.headers.get("Content-type", ""):
            image = Image.open(BytesIO(response._content))
            return image
        else:
            raise Exception("reponse not an image, api may have sent a error messeage")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed request: {e}")
def main():
    """Main loop for user interaction, 
    for text to image generation
    """
    print("welcom to text-to-image generator")
    print("type exit to quit")
    while True:
        prompt = input("Enter a description for the image u want to generate : \n").strip()
        if prompt.lower("q") == "exit":
            print("Goodbye")
            break
    