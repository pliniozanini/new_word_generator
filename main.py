import streamlit as st
import json
import numpy as np


# read json file as a dictionary
with open('new_words.json') as f:
    data = json.load(f)

# sample a key from the data dictionary in random fashion
sample_key = np.random.choice(list(data.keys()))

st.write(f"Word: {sample_key}")
st.write(f"Meaning: {data[sample_key]}")
