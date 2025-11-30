import requests
BASE_URL = "https://uselessfacts.jsph.pl/category/{}.json?language=en"
def get_fact(category):
    try:
        url = BASE_URL.format(category)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n {data['text']}\n")
        else:
            print("category not found or an api error")
    except:
        print("Failed to fetch\n")
categories = ["science","Technology","History","Food","Animals","food"]

print("Useless facts explorer")
print("Select a categorie or type q to quit\n")
for i, c in enumerate(categories,1):
    print(f"{i}. {c}")
while True:
    choice = input("\nCategorie number : ")
    if choice.lower() == "q":
        print("Goodbye")
        break
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected = categories[int(choice) - 1]
        print(f"\n Fetching {selected} fact.")
        get_fact(selected)
    else:
        print("Invalid choice : try again")