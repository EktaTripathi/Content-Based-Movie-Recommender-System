# Movie Recommender System

This project is a content-based movie recommender system developed using Python and the Streamlit library. The recommender system is built on the Kaggle TMDb 5000 Movie Dataset, providing personalized movie recommendations based on user preferences.
The recommender system suggests movies similar to a selected movie based on their content features such as plot summaries, cast, directors, and genres. It employs cosine similarity to determine movie similarity and fetches movie details using the TMDB API.

# Deployment
The recommender system is deployed on Render and can be accessed [here](https://movie-recommender-system-g1kt.onrender.com/)

# Data Source
The project utilizes the TMDB 5000 Movie Dataset, available on Kaggle. The dataset contains detailed information about movies, including metadata, cast, crew, and user ratings.
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

# Features:

- Utilizes natural language processing techniques to analyze movie descriptions and extract relevant features.
- Select a movie from the dropdown menu to get personalized recommendations.
- Recommends top 5 similar movies based on content features.
- Displays movie posters and details including overview, cast, director, and rating for each recommendation.

# Technologies and Tools:

- Python
- Streamlit
- Pandas
- Scikit-learn

## How to Run Locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/EktaTripathi/Content-Based-Movie-Recommender-System.git

2. Navigate to the project folder:
   ```bash
   cd Content-Based-Movie-Recommender-System

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app:
   ```bash
   streamlit run app.py

5. Open your web browser and go to http://localhost:8501 to access the locally running Movie Recommender System.
