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
    page_options = ["Recommender System","EDA","Solution Overview", "Meet the Team", "About Us"]

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
        st.markdown('We employed two methods of building recommmendation system:')
        st.markdown('1. Content-based filtering')
        st.markdown('2. Collaborative filtering')
        st.markdown("The Content-Based Recommendation system computes similarity between movies based on movie genres using the selected movie as a baseline. Using this type of movie recommendation system, we require the title of the movie as input, but our sim_matrix is based on the index of each movie. Therefore, to build this, we need to convert movie title into movie index and movie index into movie title. Let's create functions which operate those functions.")
        st.markdown("Collaborative methods for recommender systems are methods that are based solely on the past interactions recorded between users and items in order to produce new recommendations. These methods do not require item meta-data like their content-based counterparts. This makes them less memory intensive which is a major plus since our dataset is so huge.")
        st.markdown("Our best perfoming solution to a movie recommender sytem was the collaborative filtering. We intergrated it with our best perfoming model which is the SVD model as seen in the graph below.")
        st.subheader('A graph of Model Perfomances')
        st.image('resources/imgs/Models.jpeg',use_column_width=True)
        st.markdown('From the image above the SVD model perfomed best with an RMSE of 0.906 as compared to the other models.')
        st.markdown('The singular value decomposition (SVD) provides another way to factorize a matrix, into singular vectors and singular values. The SVD allows us to discover some of the same kind of information as the eigen decomposition.The SVD is used widely both in the calculation of other matrix operations, such as matrix inverse, but also as a data reduction method in machine learning. SVD can also be used in least squares linear regression, image compression, and denoising data.')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    # Building out the predication page
    if page_selection == "EDA":
        st.title("EDA")
        st.write("Exploratory Data Analysis")
        st.info("This will be an exploration and explanation of the dataset used and insights derived respectively")
        st.subheader('1) Genres distribution')
        st.image('resources/imgs/Distribution of genres.png',use_column_width=True)
        st.markdown('Dramatic and comic movies seem to be most popular with the Film-noir and Imax being the least popular as observed in this movies sample data.')
        
        st.subheader('2) Weekly ratings distribution')
        st.image('resources/imgs/Ratings_per_day_of_the_week.jpeg',use_column_width=True)
        st.markdown('Assuming ratings translate to viewership, from the graph we can see that viwership is at its peak during the weekend and lowest on Wednesday. Clearly Wednesday is a bad day to launch a new movie.')
        
        st.subheader('3) Ratings per user distribution')
        st.image('resources/imgs/Top_rating_users.png',use_column_width=True)
        st.markdown("Movies is business and watching movies seems to be UserId - 72315's main business. His viewership rate by far exceeds the average viewer's capacity. We treated this exceptional customer as an outlier during the modelling process inorder to improve the model's accuracy.")
        
        st.subheader('4) Top rated movies distribution')
        st.image('resources/imgs/Top_rated_movies.png',use_column_width=True)
        st.markdown("The ten top rated movies are movies from the 90's. It begs the question on whether the quality of movies has declined over the years or whether most of the customers are oldies who like to go back in time 😉🤔?")
        
        st.subheader('5) Movie titles on word cloud')
        st.image('resources/imgs/Word_cloud.png',use_column_width=True)
        st.markdown('From the word cloud visualization of titles, some of the words that seem to stand out are; love, night, man, girl, life, world, movie, death etc this corresponds to what was seen earlier on genres distribution, that the most popular movies are daramatic and comic ones. ')
        
        st.subheader('6) Average count per unique rating')
        st.image('resources/imgs/Average_count_per_rating.png',use_column_width=True)
        st.markdown('From the graph we can see that most of the ratings seem to lie in the range of 3.0 - 5.0. From this we can tell that most customers tend to rate a movie if they liked it and rarely if they did not.')

    # Building out the "Meet The Team" page
    if page_selection == "Meet the Team":
        st.subheader("Meet the Team")
        
        
        st.image('resources/imgs/company.jpg', caption="Photo Credit: Hello I'm, AI Inc.com")

		# You can read a markdown file from supporting resources folder
        st.markdown("""
		
		Our team consists of 5 talented data scientists and developers from various parts of Africa.
        You can reach out to anyone of them through the provided mails: """) 
        
        
        st.write('Israel Ezema (Nigeria): ezysticks@aiinc.com')
        st.write('Michael Omosebi  (Nigeria): omosebi@aiinc.com')
        st.write('Precious Orekha (Nigeria): orekha@aiinc.com')
        st.write('Damilare Nughes  (Nigeria): dare@aiinc.com')
        st.write('Dorcas Solonka    (Kenya): dory@aiinc.com')
		

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


    



if __name__ == '__main__':
    main()
