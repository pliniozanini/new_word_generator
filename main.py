import streamlit as st
import json
import numpy as np


# read json file as a dictionary
with open('new_words.json') as f:
    data = json.load(f)

button = st.button('Teach me a new word !!')

if button:
    # sample a key from the data dictionary in random fashion
    sample_key = np.random.choice(list(data.keys()))

    # st.write(f"Word: {sample_key}")
    # st.write(f"Meaning: {data[sample_key]}")

    # Custom CSS for styling
    st.markdown("""
        <style>
        .title {
            font-family: 'Times New Roman', serif;
            font-size: 48px;
            margin-bottom: 0;
        }
        .phonetic {
            font-family: 'Times New Roman', serif;
            font-size: 24px;
            color: gray;
            margin-top: 0;
        }
        .meaning {
            font-family: 'Times New Roman', serif;
            font-size: 18px;
            color: gray;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Display the title
    st.markdown(f"<div class='title'>{sample_key}</div>", unsafe_allow_html=True)

    # # Display the phonetic transcription
    # st.markdown("<div class='phonetic'>[ˈfɛrnve]</div>", unsafe_allow_html=True)

    # Display the meaning of the word
    st.markdown(f"<div class='meaning'>{data[sample_key]}</div>", unsafe_allow_html=True)

