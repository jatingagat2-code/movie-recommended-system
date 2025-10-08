Movie Recommender System

A content-based Movie Recommendation System built using Python, Gradio, and the TMDb API, which suggests the top 5 similar movies based on a selected movie.

🚀 Live Demo

👉 View on Hugging Face Spaces

🧠 Project Overview

This project recommends similar movies by analyzing precomputed similarity data derived from movie metadata (such as genres, cast, and crew).
Users can select a movie and instantly view the top 5 similar films along with their posters.

⚙️ Tech Stack

Python 3.10+

Pandas – for data handling

Requests – for API calls to TMDb

Gradio – for creating the interactive web interface

Pickle – for loading preprocessed data (movie_dict.pkl, similarity.pkl)

TMDb API – for fetching movie posters

🧩 How It Works

The dataset is preprocessed into:

movie_dict.pkl – contains movie IDs and titles

similarity.pkl – stores cosine similarity scores between movies

The user selects a movie from a dropdown menu.

The system:

Finds the index of the selected movie

Retrieves the top 5 most similar movies

Fetches posters from TMDb API

Displays results using a Gradio gallery interface

🧾 Files in This Repository
File	Description
app.py	Main Python application file (Gradio interface)
movie_dict.pkl	Pickled movie metadata dictionary
similarity.pkl	Precomputed movie similarity matrix
requirements.txt	List of Python dependencies
movie-recommender-system.ipynb	Jupyter notebook used for model creation
.gitattributes	Git attributes configuration
README.md	Project documentation (this file)
🧰 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Jatin1122/movie_recommendation.git
cd movie_recommendation

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
python app.py


Then open your browser at:

http://127.0.0.1:7860

🌐 Deployment on Hugging Face

This project is live on Hugging Face Spaces using the Gradio SDK.
Every commit to this GitHub repository automatically triggers a rebuild of the Space.

🔑 Environment Variables

You’ll need a TMDb API key to fetch posters.

Create an account on The Movie Database (TMDb)
 and replace the API key inside:

api_key = "YOUR_API_KEY"

✨ Example Output

Input: 🎥 Inception
Output:
A gallery of 5 similar movies with posters, such as:

Interstellar

The Prestige

Memento

The Matrix

Shutter Island

🧑‍💻 Author

Jatin Gagat
📍 Data Science & Machine Learning Enthusiast
🔗 Hugging Face Profile

🔗 GitHub

🪪 License

This project is open-source and available under the MIT License
.# movie-recommended-system
