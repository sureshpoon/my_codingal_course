import requests 
import html
import random
url = "https://opentdb.com/api.php?amount=5&type=multiple"
response = requests.get(url)
if response.status_code == 200 :
    trivia_data = response.json()
    score = 0
    for i, question_data in enumerate(trivia_data["results"]) :
        question_text = html.unescape(question_data["question"])
        print(f"question{i + 1} : {question_text}")
        options = question_data['incorrect_answers'] + [question_data['correct_answer']]
        options = [html.unescape(option) for option in options]
        random.shuffle(options)
        for j, option in enumerate(options) :
            print(f"{j + 1}.{option}")
        while True:
            try :
                user_answer = input("Your answer (1-4) : ")
                user_choice = int(user_answer) 
                if 1 <= user_choice <= 4 :
                    break
                else :
                    print("Please enter a number between 1 and 4")
            except ValueError :
                print("Please enter a valid number")
        correct_answer = html.unescape(question_data['correct_answer'])
        if options [user_choice - 1] == correct_answer :
            print("Correct answer")
            score = score + 1 
        else :
            print(f"Wrong answer, the correct answer is : {correct_answer}")
    print(f"\n Your final score is : {score} / {len(trivia_data['results'])}")
else :
    print(f"Failed to retrieve data, status code : {response.status_code}")            

