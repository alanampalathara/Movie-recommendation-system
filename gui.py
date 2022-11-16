import numpy as np
import pandas as pd
import difflib
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
warnings.filterwarnings("ignore")
import streamlit as st
import base64



movies = pd.read_csv('C:/Users/alant/Documents/ML2 Project/data/movies.csv',sep=';',encoding='latin-1').drop('Unnamed: 3',axis=1)
ratings = pd.read_csv('C:/Users/alant/Documents/ML2 Project/data/ratings.csv',sep=';')
users = pd.read_csv('C:/Users/alant/Documents/ML2 Project/data/users.csv',sep=';')


vectorizer = CountVectorizer(stop_words='english')
genres = vectorizer.fit_transform(movies.genres).toarray()
contents = pd.DataFrame(genres,columns=vectorizer.get_feature_names())

nn_algo = NearestNeighbors(metric='cosine')
nn_algo.fit(contents)


    
# This method will recommend movies based on a movie that passed as the parameter
def recommend_on_movie(movie,hist,n_reccomend = 5):
    iloc = movies[movies['title']==movie].index[0]
    distance,neighbors = nn_algo.kneighbors([contents.iloc[iloc]],n_neighbors=n_reccomend+1)
    recommeds = [movies.iloc[i]['title'] for i in neighbors[0] if i not in [iloc]]
    return recommeds[:n_reccomend]

# This method will recommend movies based on history stored in self.hist list
def recommend_on_history(hist,n_reccomend = 5):
    history = np.array([list(contents.iloc[iloc]) for iloc in hist])
    distance,neighbors = nn_algo.kneighbors([np.average(history,axis=0)],n_neighbors=n_reccomend + len(hist))
    recommeds = [movies.iloc[i]['title'] for i in neighbors[0] if i not in hist]
    return recommeds[:n_reccomend]




def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 100% 100%;

    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('C:/Users/alant/Documents/ML2 Project/movie_bg.png')  






    
#st.title('Movie Recommendation System')
st.markdown(f'<h1 style="color:#BF0000;background-color: rgba(255, 255, 255, 0.9);font-size:48px;border-radius:3%;">{"Movie Recommendation System"}</h1>', unsafe_allow_html=True)
# getting the movie name from user
#movie_name = st.text_input('Movie Name')0000000
option = st.selectbox(
 '', tuple(['']+movies['title'].tolist()))


#list_of_all_titles = movies['title'].tolist()
if "history" not in st.session_state:
    st.session_state["history"]=[]
#find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
#close_match = find_close_match[0]
if st.button('Find Recommendation'):
    col1, col2 = st.columns(2)
    st.session_state["history"].append(movies[movies['title']==option].index[0])
    recom =recommend_on_movie(option, st.session_state["history"])
    hist_recom = recommend_on_history(st.session_state["history"])
    with col1:
        st.markdown(f'<h2 style="color:#FFFFFF;background-color:#111111;font-size:15px;border-radius:0%;">{"Recommended movies"}</h3>', unsafe_allow_html=True)
        for mov in recom:
            st.markdown(f'<h2 style="color:#FFFFFF;background-color: rgba(100, 100, 100, 0.95);font-size:14px;border-radius:0%;">{"*  "+mov}</h3>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<h2 style="color:#FFFFFF;background-color:#111111;font-size:15px;border-radius:0%;">{"Recommended movies from history"}</h3>', unsafe_allow_html=True)
        for mov in hist_recom:
            st.markdown(f'<h2 style="color:#FFFFFF;background-color: rgba(100, 100, 100, 0.95);font-size:14px;border-radius:0%;">{"*  "+mov}</h3>', unsafe_allow_html=True)
            

#filter: blur(8px);
 # -webkit-filter: blur(8px);

