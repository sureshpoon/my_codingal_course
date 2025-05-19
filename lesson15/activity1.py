import colorama 
from colorama import Fore, Style
from textblob import TextBlob #processes the text
colorama.init()
print(f"{Fore.CYAN} Welcome to sentiment spy {Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA} Enter your name : {Style.RESET_ALL}")

if not user_name :
    user_name = "Anonymous"

conversation = []
print (f"\n {Fore.CYAN} hello, {user_name}" )
print("Type a sentence and i will analyze your sentence")
print(f"Type {Fore.YELLOW} 'reset' {Fore.CYAN}, {Fore.YELLOW} 'history' {Fore.CYAN}," 
      f" or {Fore.YELLOW} 'exit' {Fore.CYAN} to quit {Style.RESET_ALL} \n")
while True :
    user_input = input (f"{Fore.GREEN} -- {Style.RESET_ALL}")
    if not user_input.strip() :
        print (f"{Fore.RED} Please enter a valid sentence {Style.RESET_ALL}")
        continue 
    if user_input.lower() == "exit" :
        print(f"\n {Fore.BLUE} Exiting the sentiment spy {Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset" :
        conversation.clear()
        print(f"{Fore.CYAN} All history got deleted {Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history" :
        if not conversation :
            print (f"{Fore.YELLOW} No conversation history yet {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation history : {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation, start = 1) :
                if sentiment_type == "Positive" :
                    color = Fore.GREEN
                elif sentiment_type == "Negative" :
                    color = Fore.RED 
                else :
                    color = Fore.YELLOW 
                print (f"{idx}. {color}{text}" f"polarity : {polarity : .2f}, {sentiment_type} {Style.RESET_ALL}")
        continue   
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25 :
        sentiment_type = "Positive"
        color = Fore.GREEN 
    elif polarity < - 0.25 : 
        sentiment_type = "negative"
        color = Fore.RED 
    else :
        sentiment_type = "neutral"
        color = Fore.YELLOW
    conversation.append((user_input , polarity, sentiment_type ))
    print (f"{color}{sentiment_type} sentiment detected " f"polarity : {polarity : .2f} {Style.RESET_ALL}")                         

