import pandas as pd, random, time, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore, Style
init(autoreset=True)


def load_data(path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(path)
        df['combined'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"File {path} not found."); sys.exit()

movies = load_data()
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])
cosine_sim = cosine_similarity(tfidf_matrix)

def list_genres(df): return sorted({g.strip() for x in df['Genre'].dropna() for g in x.split(',')})
genres = list_genres(movies)


def recommend(genre=None, mood=None, rating=0, top_n=5):
    df = movies.copy()
    if genre: df = df[df['Genre'].str.contains(genre, case=False, na=False)]
    if rating: df = df[df['IMDB_Rating'] >= rating]
    df = df.sample(frac=1)
    recs = []
    for _, r in df.iterrows():
        if not mood:
            recs.append((r['Series_Title'], TextBlob(r['Overview']).sentiment.polarity))
        else:
            movie_sentiment = TextBlob(r['Overview']).sentiment.polarity
            mood_sentiment = TextBlob(mood).sentiment.polarity
            if mood_sentiment * movie_sentiment >= 0:
                recs.append((r['Series_Title'], movie_sentiment))
    return recs[:top_n] if recs else "No suitable movie recommendations found."

def show(recs, name):
    if isinstance(recs, str):
        print(Fore.RED + recs)
        return
    print(Fore.YELLOW + f"\n AI Recommendations for {name}:")
    for t, p in recs: 
        sentiment = 'Positive' if p > 0 else 'Negative' if p < 0 else 'Neutral'
        print(f"- {t} ({sentiment})")

def main():
    print(Fore.BLUE + " Welcome to AI Movie Assistant!\n")
    name = input(Fore.YELLOW+"Your name: ").strip()
    print(Fore.GREEN+f"Great to meet you, {name}!\n\nAvailable Genres:")
    [print(f"{i+1}. {g}") for i,g in enumerate(genres)]
    while True:
        g = input(Fore.YELLOW+"choose genre (or press enter to skip): ").strip()
        g = g if g in genres else None
        mood = input(Fore.YELLOW+"Mood (describe how you feel): ").strip()
        r = input(Fore.YELLOW+"Minimum rating (0-10): ").strip()
        r = float(r) if r.replace('.', '').isdigit() else 0
        show(recommend(g, mood, r), name)
        
        if input(Fore.YELLOW+"\nMore recommendations? (yes/no): ").lower()!="yes":
            print(Fore.GREEN+f"Enjoy your movie, {name}! "); break
if __name__=="__main__": main()