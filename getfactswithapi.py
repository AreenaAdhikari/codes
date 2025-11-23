import requests
url = "https://uselessfacts.jsph.pl/random.json?language=en"
def get_random_technology_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to Fetch data")
while True:
    user_input = input("Press enter to get a random fact or else press 'q' to quit the game... :  ")
    if user_input.lower() == 'q':
        break
    get_random_technology_facts()

