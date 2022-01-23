import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("marvel.csv", header=None)
df.columns = ["Title", "Year", "Directors", "Casting", "Genre", "Main Actor Name",
              "Main Actor Birthdate", "Main Actor Height", "Main Actor Fun Fact", "Main Actor Other Movies", "Movie_ID"]
marvel_movie_order = (3, 5, 4, 6, 1, 7, 8, 9, 10, 11, 13, 14, 15, 17, 12, 16, 20, 19, 22, 21, 2, 23, 25, 18, 24, 27, 26)
important_columns = ['Casting', 'Directors', 'Main Actor Name', 'Genre', 'Title']
df["marvel_movie_order"] = marvel_movie_order

def get_important_features(data):
    important_features = []
    for i in range(0, data.shape[0]):
        important_features.append(data['Casting'][i]+' '+data['Directors'][i]+' '+data['Main Actor Name'][i]+
                                  ' '+data['Genre'][i]+' '+data['Title'][i])
    return important_features


df['important_features'] = get_important_features(df)
cm = CountVectorizer().fit_transform(df['important_features'])
cs = cosine_similarity(cm)

recommande = {}
def recommandation(movie):
    title = movie
    movie_id = df[df.Title == title]['Movie_ID'].values[0]
    scores = list(enumerate(cs[movie_id]))
    sorted_scores = sorted(scores, key= lambda x:x[1], reverse = True)
    sorted_scores = sorted_scores[1:]

    j = 0
    print("The 3 mmost recommanded movies to", title, 'are:\n')
    for item in sorted_scores:
        movie_title = df[df.Movie_ID == item[0]]['Title'].values[0]
        print(j+1, movie_title)
        recommande[j+1] = movie_title
        j +=1
        if j >2:
            break
    return recommande
    
if __name__ == "__main__":
    print(recommandation("Avengers: Infinity War"))