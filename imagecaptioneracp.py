import requests
from requests.auth import HTTPBasicAuth
API_KEY = "acc_6cdd73f85374705"
API_SECRET = "87e9482d85d8a33163638d934cbe3d56"
def simple_describe_image(image_path, tag_count=15):
    url = "https://api.imagga.com/v2/tags"
    with open(image_path, "rb") as img:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(API_KEY, API_SECRET),
            files={"image": img}
        )
    data = response.json()
    tags = data["result"]["tags"][:tag_count]
    tag_words = [tag["tag"]["en"] for tag in tags]
    description = "This image contains " + ", ".join(tag_words[:-1]) + f", and {tag_words[-1]}."
    print("\nImage Description:")
    print("-" * 30)
    print(f"Image: {image_path}")
    print(f"Description: {description}")
    print(f"Approximate words: {len(description.split())}")
    return description
def main():
    image_path = input("Enter image path: ")
    simple_describe_image(image_path)
if __name__ == "__main__":
    main()