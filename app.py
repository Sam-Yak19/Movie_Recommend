import streamlit as st
import pickle
import pandas as pd
import requests

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url(https://storage.googleapis.com/kaggle-datasets-images/3375918/5872805/e6c438e764799de9a90ae10bd32c51cc/dataset-cover.jpg?t=2023-06-08-06-58-37);
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8d61596cc6eced01d1369f27ad0b512b'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+ data['poster_path']
st.title("Movie Recommender System")

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movie=[]
    recommended_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster

movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
selected_movie_name= st.selectbox(
    "Enter the movie name : ",
    movies['title'].values)


st.button("Reset", type="primary")
if st.button("Recommend"):
    names,posters=recommend(selected_movie_name)

    st.subheader("Top Recommendations")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"**{names[0]}**")
        st.image(posters[0])

    with col2:
        st.markdown(f"**{names[1]}**")
        st.image(posters[1])

    with col3:
        st.markdown(f"**{names[2]}**")
        st.image(posters[2])

    with col4:
        st.markdown(f"**{names[3]}**")
        st.image(posters[3])

    with col5:
        st.markdown(f"**{names[4]}**")
        st.image(posters[4])

    # Add spacing between rows
    st.markdown("<br>", unsafe_allow_html=True)

    # Second row of posters (5-9)
    st.subheader("More Recommendations")
    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.markdown(f"**{names[5]}**")
        st.image(posters[5])

    with col7:
        st.markdown(f"**{names[6]}**")
        st.image(posters[6])

    with col8:
        st.markdown(f"**{names[7]}**")
        st.image(posters[7])

    with col9:
        st.markdown(f"**{names[8]}**")
        st.image(posters[8])

    with col10:
        st.markdown(f"**{names[9]}**")
        st.image(posters[9])