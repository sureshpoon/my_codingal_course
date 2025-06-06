# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer 
# from sklearn.metrics.pairwise import cosine_similarity 
# from textblob import TextBlob
# from colorama import Fore, Style, init 
# import time #animation 
# init(autoreset = True) 
# #loading the dataset

# def load_data(file_path = "imdb_top_1000.csv") :
#     try :
#         df = pd.read_csv(file_path)
#         df['combine_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('') 
#         return df
#     except FileNotFoundError :
#         print (Fore.RED + "Error: File not found! " )
#         exit()

# movies_df = load_data() 

# #vectorizing the combine feature coloumn
# tfidf = TfidfVectorizer (stop_words = 'english')
# tfidf_matrix = tfidf.fit_transform(movies_df['combine_features']) #transforms in matrix form
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# # list all the unique genres 
# def list_genres(df) :
#     return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist ))
# genres = list_genres(movies_df)

# #recommend movies based on the filters 
# def recommend_movie(genre = None, mood = None, rating = None, top_n = 5) :
#     filter_df = movies_df()
#     if genre:
#         filter_df = filter_df[filter_df['Genre'].str.contains(genre, case = False, na = False)]
#     if rating :
#         filter_df = filter_df[filter_df['IMDB_Rating']>= rating] 
#     filter_df = filter_df.sample(frac = 1).resetindex(drop = True) 
#     recommendation = []
#     for idx, row in filter_df.iterrows() :
#         overview= row['Overview']
#         if pd.isna(overview) :
#             continue
#         polarity = TextBlob(overview).sentiment.polarity
#         if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0.6 )) or not mood :
#             recommendation.append((row['Series_Title'], polarity ))
#             if len (recommendation)== top_n :
#                 break 
#     return recommendation if recommendation else "No suitable movies found"        
# #display recommendation 
# def display_recommendation(recs, name) :
#     print (Fore.YELLOW + f"\n AI analyze movie recommendations for {name} : " )
#     for idx, (title, polarity) in enumerate(recs , 1) :
#         sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
#         print (f"{Fore.CYAN} {idx}. {title} (polarity : {polarity : .2f }, {sentiment} ) ") 

# #Small processing animation
# def processing_animation() :
#     for _ in range (3) :
#         print (Fore.YELLOW + "." , end = "", flush = True)
#         time.sleep(0.5)
#     print ()

# #Ai recommendation flow 
# def handle_AI (name) :
#     print (Fore.BLUE + "\n Let's find the perfect movie for you \n")
#     print (Fore.GREEN + "Available genres : ", end = "")
#     for idx, genre in enumerate (genres, 1):
#         print (f"{Fore.CYAN} {idx.genres} ")
#     while True :
#         genre_input = input (Fore.YELLOW + "Enter the genre number : ".strip())
#         if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres) :
#             genre = genres [int(genre_input) -1] 
#         else:
#             genre = genre_input 
#         mood = input (Fore.YELLOW + "Whats your mood?(Happy,sad, adventerous, etc.)?".strip())
#         try : 
#             rating = float(input (Fore.YELLOW + "Minimum imdb rating (E.g. 7.0) : " ).strip()) 
#         except ValueError :
#             rating = None
#         print (Fore.GREEN + "\n analyzing your mood and preferences ", end = "")
#         processing_animation()
#         recommendations = recommend_movie(genre = genre, mood = mood , rating = rating )
#         display_recommendation(recommendations, name)
#         cont = input (Fore.YELLOW + "\n Would you like more recommendations ? (yes / no) : ").strip().lower()
#         if cont != 'yes':
#             break

# if __name__ == " __main__ " :
#     user_name = input (Fore.YELLOW + "Enter your name : ").strip()
#     handle_AI(user_name)
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, Style, init
import time  # animation

init(autoreset=True)

# Load the dataset
def load_data(file_path="imdb_top_1000.csv"):
    try:
        df = pd.read_csv(file_path)
        df['combine_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + "Error: File not found!")
        exit()

movies_df = load_data()

# Vectorizing the combined features column
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combine_features'])  # transforms to matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# List all the unique genres
def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist))

genres = list_genres(movies_df)

# Recommend movies based on filters
def recommend_movie(genre=None, mood=None, rating=None, top_n=5):
    filter_df = movies_df

    if genre:
        filter_df = filter_df[filter_df['Genre'].str.contains(genre, case=False, na=False)]

    if rating:
        filter_df = filter_df[filter_df['IMDB_Rating'] >= rating]

    filter_df = filter_df.sample(frac=1).reset_index(drop=True)

    recommendation = []

    for idx, row in filter_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue

        polarity = TextBlob(overview).sentiment.polarity

        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0.6)) or not mood:
            recommendation.append((row['Series_Title'], polarity))

        if len(recommendation) == top_n:
            break

    return recommendation if recommendation else "No suitable movies found."

# Display recommendations
def display_recommendation(recs, name):
    print(Fore.YELLOW + f"\nAI-analyzed movie recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
        print(f"{Fore.CYAN}{idx}. {title} (Polarity: {polarity:.2f}, Sentiment: {sentiment})")

# Small processing animation
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
    print()

# AI recommendation flow
def handle_AI(name):
    print(Fore.BLUE + "\nLet's find the perfect movie for you\n")
    print(Fore.GREEN + "Available genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")

    while True:
        genre_input = input(Fore.YELLOW + "Enter the genre number or name: ").strip()

        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input) - 1]
        else:
            genre = genre_input

        mood = input(Fore.YELLOW + "What's your mood? (Happy, Sad, Adventurous, etc.): ").strip()

        try:
            rating = float(input(Fore.YELLOW + "Minimum IMDb rating (e.g., 7.0): ").strip())
        except ValueError:
            rating = None

        print(Fore.GREEN + "\nAnalyzing your mood and preferences", end="")
        processing_animation()

        recommendations = recommend_movie(genre=genre, mood=mood, rating=rating)

        if isinstance(recommendations, str):
            print(Fore.RED + recommendations)
        else:
            display_recommendation(recommendations, name)

        cont = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

# Entry point
if __name__ == "__main__":
    user_name = input(Fore.YELLOW + "Enter your name: ").strip()
    handle_AI(user_name)





          




