import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
from colorama import Fore,init,Style
import os
init(autoreset=True)
API_KEY ="acc_6cdd73f85374705"
API_KEY_SECRET= "87e9482d85d8a33163638d934cbe3d56"
IMAGGA_URL = "https://api.imagga.com/v2/tags"

def trucated_text(text,word_limit):
    words = text.split()
    return"".join(words[:word_limit])
def get_image_tags(image_path,limit=10):
    with open(image_path, "rb") as img:
        response = requests.post(
            IMAGGA_URL,
            auth=HTTPBasicAuth(API_KEY,API_KEY_SECRET),
            files={"image":img}
        )
    data = response.json()
    tags = data.get("result",{}).get("tags",[]) 
    return [tag["tag"]["en"]for tag in tags[:limit]]
def generate_caption(tags):
    return trucated_text(",".join(tags),5)
def generate_description(tags):
    sentence=(
        f"this scene shows{tags[0]}."
        f"it includes elements such as {",".join(tags[1:6])}."
        f"this scene appears visually clear and well composed"
    )
    return truncated_text(sentence,30)
def generate_summary(tags):
    sentence=(
        f"The image primarly feature{tags[0]}."
        f"Other visible elements include{",".join(tags[1:7])}."
        f"The objects are clearly distinguisable and from a meningfull scene"
        f"the image is a beautiful repersentation which is stunning"
    )
def print_menu():
    print(f"""{Style.BRIGHT}{Fore.GREEN}
          Select one of these following outputs:
          1.Caption(5 words)
          2.Description(30 words)
          3.Summary (50 words)
          4.exit
          """)
    