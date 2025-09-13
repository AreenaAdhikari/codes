import re,random
from colorama import Fore,init
init(autoreset=True)
destinations = {

    "Mountains": ["Swiss Alps","Himalayas","Rocky Mountains"],
    "Beaches": ["Bali","Maldives","Phuket"],
    "cities" : ["tokyo","New york","Paris"]
}

jokes=[
    "Why do programmers hate going outside?,There are too many bugs ",
    "Why did the computer go to the doctors?It had virus",
    "Why do travelers , they have hot spots "
]
def normalize(text): return re.sub(r"\s+","".text.strip().lower())
def recommend():
    pref = normalize(input(f"{Fore.CYAN} TRAVEL BOT: beaches , mountains or cities? /n{Fore.YELLOW}You: "))
    if pref in destinations :
        suggestions = random.choice(destinations[pref])
        print(f"{Fore.GREEN}How about {suggestions}!?")
        ans = input(f"{Fore.YELLOW}You : (yes/no)").lower()
        if ans == "yes" : return print(f"{Fore.GREEN}Awsome ,enjoy {suggestions}! ")
        if ans == "no" : continue
        return
    else:
        print(f"{Fore.RED} Sorry i dont know that type of destinations")
    
def packing():
    loc = normalize(print(f"{Fore.CYAN} where are u going to \n"{Fore.YELLOW}"You: "))
    days = input(f"{Fore.CYAN} How many days are u going for \n " {Fore.YELLOW} "You : ")
    print(" Packing tips for {days} days in {loc}")
    print("-Pack versitile clothes -- bring charger/adapter-- Always check weather forecasts")

def tell_joke(): print("Travel Bot : {random.choice(jokes)}")
def show_help ():
    print("\n I can  suggests travel spots("recomendation") offer packing tip("packing") tell a joke("jokes")exit("exit")")
