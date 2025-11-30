import requests

Base_url = "https://uselessfacts.jsph.pl/random.json?language=en"
def get_fact(category):
    try:
        url = Base_url.format(category)
        response = requests.get(Base_url)
        if response.status_code == 200 :
            data = response.json()
            print(f"\n {data['text']}\n")
        else:
            print("Category not found or an api error")
    except:
        print("Failed to fetch data")
categories = ["Technology","Food","Science","Random","Animals","Histroy"]
print("Useless facts explorer")
print("Select A Category or type 'q' to quit\n")
for i,c in enumerate(categories,1):
    print(f"{i}. {c}")
while True:
    choice = input("\n Enter Categorie  1-4")
