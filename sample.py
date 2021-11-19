import streamlit as st

import pandas as pd
import numpy as np

PATH = 'media/AB_NYC_2019.csv'

menu = ['Home', 'Read Data',
        'About me']

choice = st.sidebar.selectbox('What puppy can do?', menu)

if choice=='Home':
    st.title("Puppy Wonderland")
    st.header("My first app")

    st.write("")
    st.write("My puppy can do anything!")

    st.image('media/isle_of_dog.gif',
            caption="My lovely black puppy",
            use_column_width='auto')

    col1, col2 = st.columns(2)

    # NAME
    with col1:
        name = st.text_input('Enter your puppy name:')
        if name!="":
            st.write(name, 'is a cute name!')

    # AGE
    with col2:
        age = st.slider('Choose your puppy age', min_value=1, max_value=20)
        st.write('Your puppy is', age, 'years old!')

elif choice=='Read Data':
    # Cache the function output
    @st.cache()
    def load_data(path):
        return pd.read_csv(path)
    
    st.title('Hot Dog Summer!')
    st.image('media/dog-beach-lifesaver.png')

    df = load_data(PATH) 
    st.dataframe(df)