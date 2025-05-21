import re, random 
from colorama import Fore, init
init (autoreset = True) 
destinations = {
    "beaches" : ["Bali", "Maldives", "Phuket"],
    "mountains" : ["Swiss alps", "Rocky mountains", "Himalayas"],
    "cities" : ["Tokyo", "Paris", "New york"]
}
jokes = [
    "Why dont programs like nature ? too many bugs",
    "Why did the computer go to the doctor ? it had a virus",
    "Why do travellers always feel warm ? because of all their hot spots"
]
def normalize_input(text):
    return re.sub (r"\s+", " ", text.strip().lower())

def recommend():
    print (Fore.CYAN + "Travel bot : Beaches, Mountains, Cities?")
    preference = input (Fore.YELLOW + "You : ")
    preference = normalize_input (preference)
    if preference in destinations :
        suggestions = random.choice(destinations [preference])
        print (Fore.GREEN + f"Travel bot : How about {suggestions} ?")
        print(Fore.CYAN + "Travel bot : Do you like it? (yes or no)")
        answer = input (Fore.YELLOW + "You : ").lower()
        if answer == "yes":
            print (Fore.GREEN + f"Travel bot : Awesome ! Enjoy {suggestions} ")
        elif answer == "no" :
            print (Fore.RED + f"Travel bot : Lets try another ")
            recommend()
        else :
            print (Fore.RED + "Travel bot : I'll suggest again")   
            recommend()

    else :
        print (Fore.RED + "Travel bot : Sorry, I don't have that type of destinations") 
    show_help()

def packing_tips() :
    print (Fore.CYAN +"Travel bot : Where to?")
    location = normalize_input (input(Fore.YELLOW + "You : "))
    print (Fore.CYAN + "Travel bot : How many days ? ")
    days = input (Fore.YELLOW + "You : ")
    print (Fore.GREEN + f"Travel bot : Packing tips for {days} days in {location}")
    print (Fore.GREEN +"Pack versatile clothes")
    print (Fore.GREEN + "Bring chargers/adapters")
    print (Fore.GREEN + "Check the weather forecast")

def tell_joke ():
    print (Fore.YELLOW + f"Travel bot : {random.choice(jokes)}")

def show_help ():
    print (Fore.MAGENTA + "\n I can : ")
    print (Fore.GREEN + "Suggest travel spots")
    print (Fore.GREEN + "Offer packing tips")
    print (Fore.GREEN + "Tell a joke")
    print (Fore.CYAN + "Type 'exit' or 'bye' to end \n")

def chat() :
    print (Fore.CYAN + "Hello, I am Travel bot")
    name = input (Fore.YELLOW + "Your name ? ")
    print (Fore.GREEN + f"Nice to meet you, {name}")
    show_help() 
    while True : 
        user_input = input (Fore.YELLOW + f"{name} : ")
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input :
            recommend()
        elif "packing" in user_input or "pack" in user_input :
            packing_tips()
        elif "joke" in user_input or "funny" in user_input :
            tell_joke()
        elif "help" in user_input : 
            show_help()
        elif "exit" in user_input or "bye" in user_input :
            print(Fore.CYAN + "Travel bot : Safe travels !")
            break
        else : 
            print (Fore.RED + "Travel bot : Could you repeat ?")

if __name__== "__main__" :
    chat()             
                   
