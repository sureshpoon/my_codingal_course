import random
from colorama import Fore, init, Style
init (autoreset = True)

def play() :
    while True:
        print (Fore.CYAN + "Hello, I am your AI assistant!")
        print (Fore.MAGENTA + "I can play Rock, Paper, Scissors with you.")
        print (Fore.YELLOW + "Let's start the game!")
        print (Fore.MAGENTA+ "Welcome to Rock, Paper, Scissors with AI!" + Style.RESET_ALL)
        user_choice = input(Fore.CYAN + "Enter your choice (rock, paper, scissors): ").lower()
        computer = random.choice(["rock", "paper", "scissors"])
        print(Fore.YELLOW + f"Computer chose: {computer}")

        if user_choice == computer:
            print(Fore.GREEN + "It's a tie!" + Style.RESET_ALL)
        elif (user_choice == "rock" and computer == "scissors") or \
            (user_choice == "paper" and computer == "rock") or \
            (user_choice == "scissors" and computer == "paper"):
            print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "You lose!" + Style.RESET_ALL)
        print(Fore.MAGENTA + "Thanks for playing!" + Style.RESET_ALL)
        play_again = input(Fore.CYAN + "Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print (Fore.MAGENTA + "Thanks for playing with me!" + Style.RESET_ALL)
            break
        
if __name__ == "__main__":
    play()