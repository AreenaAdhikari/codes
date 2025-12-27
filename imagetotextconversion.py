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
        f"it includes elements such as {', '.join(tags[1:6])}."
        f"this scene appears visually clear and well composed"
    )
    return trucated_text(sentence,30)
def generate_summary(tags):
    sentence=(
        f"The image primarly feature{tags[0]}."
        f"Other visible elements include{', '.join(tags[1:7])}."
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
def main():
    image_path = input(f"{Fore.BLUE} Enter a image path: {Style.RESET_ALL}")
    if not os.path.exists(image_path):
        print(f"{Fore.RED}Image path not found")
        return
    try:
        Image.open(image_path)
    except:
        print(f"{Fore.RED}Invalid Image")
        return
    
    print(f"{Fore.YELLOW}Analyzing IMAGE .....\n")
    tags = get_image_tags(image_path)

    if not tags:
        print(f"{Fore.RED} tag not found")
        return
    while True:
        print_menu()
        choice = input("Enter a choice (1-4): ")
        if choice == "1":
            caption = generate_caption(tags)
            print(f"{Fore.YELLOW} CAPtion (5 words) : {Style.BRIGHT}{caption}\n")
        elif choice == "2":
            desc = generate_description(tags)
            print(f"{Fore.CYAN} Description (30 words): {Style.BRIGHT}{desc}\n")
        elif choice == "3":
            summary = generate_summary(tags)
            print(f"{Fore.GREEN} SUMMARY: (50 words): {Style.BRIGHT}{summary}\n")
        elif choice == "4":
            print(f"{Fore.LIGHTWHITE_EX}GOODBYE! ")
            break
        else:
            print(f"{Fore.RED}Invalid choice, enter (1-4)\n")

if __name__ == "__main__":
    main()