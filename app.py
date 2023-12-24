import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&language=en-US')
    data = response.json()
    poster_path = data.get('poster_path')
    return 'https://image.tmdb.org/t/p/w500/' + poster_path


def fetch_movie_details(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&language=en-US')
    data = response.json()
    movie_title = data.get('title')
    overview = data.get('overview')
    rating = data.get('vote_average')

    cast_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    cast_data = cast_response.json()
    director = next((crew['name'] for crew in cast_data['crew'] if crew['job'] == 'Director'), 'Not available')
    cast_list = [actor['name'] for actor in cast_data['cast'][:5]]

    return movie_title, overview, rating, director, cast_list


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Type or select a movie from the dropdown', movies['title'].values)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie_name)

    for i in range(len(names)):
        col1, col2 = st.columns([3, 3])  # Adjust the column proportions as needed
        with col1:
            if posters[i]:
                # Adjust the size of the poster using HTML img tag within st.markdown
                st.markdown(f'<img src="{posters[i]}" alt="Movie Poster {i + 1}" style="width: 300px; height: auto;">',
                            unsafe_allow_html=True)
        with col2:
            movie_title, overview, rating, director, cast_list = fetch_movie_details(
                movies[movies['title'] == names[i]]['movie_id'].values[0])
            if all([movie_title, overview, rating, director, cast_list]):
                # Styling for the movie title
                st.write(f"<h2 style='color: white;'>{movie_title}</h2>", unsafe_allow_html=True)
                st.write(f"**Overview:** {overview}\n\n"
                         f"**Cast:**\n{', '.join(cast_list)}\n\n"
                         f"**Director:** {director}\n\n"
                         f"**Rating:** {'★' * int(rating / 2)} ({rating})\n")
            else:
                st.write("Error fetching movie details.")