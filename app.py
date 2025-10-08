import pickle
import pandas as pd
import requests
import gradio as gr

# Function to fetch movie poster from TMDb API
def fetch_poster(movie_id):
    api_key = "3153325a6e5b71e3e7cb0dff3f9cf095"  # replace with your API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id   # get movie_id from dataset
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Gradio function
def recommend_ui(movie):
    names, posters = recommend(movie)
    return [(posters[i], names[i]) for i in range(5)]

# Interface
iface = gr.Interface(
    fn=recommend_ui,
    inputs=gr.Dropdown(choices=movies['title'].tolist(), label="🎥 Select a Movie"),
    outputs=gr.Gallery(label="🎬 Recommended Movies", columns=5, height="auto"),
    title="🎬 Movie Recommender System",
    description="Get top 5 movie recommendations based on similarity!"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
