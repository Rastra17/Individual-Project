import streamlit as st
import pandas as pd
import pickle

dfPickle = open("../Backend/df.pkl", 'rb')
similarityPickle = open("../Backend/similarity.pkl", 'rb')
df = pd.read_pickle(dfPickle)
similarity = pd.read_pickle(similarityPickle)

# Web App
st.title('Job Recommendation System')