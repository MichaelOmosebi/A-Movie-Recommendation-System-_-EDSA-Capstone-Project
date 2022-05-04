"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
from gettext import install
import streamlit as st


# Data handling dependencies
import pandas as pd
import numpy as np
import codecs


# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model


# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["AI Inc.","Recommender System","EDA","Solution Overview", "Meet the Team", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    # Building out the predication page
    if page_selection == "EDA":
        st.title("EDA")
        st.write("Exploratory Data Analysis")
        st.info("This will be an exploration and explanation of the dataset used and insights derived respectively")
        st.image('resources/imgs/Distribution of genres.png',use_column_width=True)
        st.markdown('Genres distribution')
        
        st.image(r'resources/imgs/Ratings_per_day_of_the_week.jpeg',use_column_width=True)
        st.markdown('Weekly ratings distribution')
        
        st.image('resources/imgs/Top_rating_users.png',use_column_width=True)
        st.markdown('Ratings per user distribution')
        
        st.image('resources/imgs/Top_rated_movies.png',use_column_width=True)
        st.markdown('Top rated movies distribution')
        
        st.image('resources/imgs/Word_cloud.png',use_column_width=True)
        st.markdown('Words distribution')
        
        st.image('resources/imgs/Average_count_per_rating.png',use_column_width=True)
        st.markdown('Average count per rating')

    # Building out the "Meet The Team" page
    if page_selection == "Meet the Team":
        st.subheader("Meet the Team")
        
        
        st.image('resources/imgs/company.jpg', caption="Photo Credit: Hello I'm, AI Inc.com")

		# You can read a markdown file from supporting resources folder
        st.markdown("""
		
		Our team consists of 5 talented data scientists and developers from various parts of Africa. These are:
		- Israel Ezema (Nigeria)
		- Michael Omosebi  (Nigeria)
		- Precious Orekha (Nigeria)
		- Damilare Nughes  (Nigeria)
		- Dorcas Solonka    (Kenya)
		""")

	# Building out the "About Us" page
    if page_selection == "About Us":
        st.subheader("AI Inc.")
		#Company logo
        st.image('resources/imgs/AI_logo.jpg', caption='Photo Credit: Israel Ezema')
		# You can read a markdown file from supporting resources folder
        st.markdown("""
		AI Inc. specializes in Information Technology Services. We take 
		data and arrange it in such a way that it makes sense for business and individual users. We also build and train models that are capable of giving data solutions by employing machine learning technology.
		
		Our team of leading data scientists work tirelessly to make your life and the life of your customers easy.
		"""
		)

        st.markdown(""" 
		For more info:
		email: info@aiinc.com
		""")

    # Building out the "Home" page
    if page_selection == "AI Inc.":
        st.subheader("AI Inc.")
		#Company logo
        st.image('resources/imgs/AI_logo.jpg', caption='Photo Credit: Israel Ezema')
    



if __name__ == '__main__':
    main()
