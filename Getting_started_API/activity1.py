import requests 

def get_random_jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200 :
        print(f"full json response : {response.json()}")
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else : 
        return "Failed to retrieve the json"
def main():
    print("Welcome to the random joke generator")
    while True :
        user_input = input("Press enter to get a new joke , or type 'q' to exit : ").strip().lower()
        if user_input == 'q' :
            break
        joke = get_random_jokes()
        print (joke) 
if __name__ == "__main__" :
    main()           