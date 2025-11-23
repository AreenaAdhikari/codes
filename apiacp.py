import requests

def get_random_joke():
    """Fetch a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    else:
        return "Could not get a joke"

def main():
    print(" Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press Enter for a new joke or //type 'q' to quit: ").strip().lower()
        if user_input in ("q", "exit"):
            print("Goodbye!")
            break
        print(get_random_joke(), "\n")

if __name__ == "__main__":
    main()