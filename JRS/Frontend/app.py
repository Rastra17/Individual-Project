import streamlit as st
import pandas as pd
import pickle

dfPickle = open("../Backend/df.pkl", 'rb')
similarityPickle = open("../Backend/similarity.pkl", 'rb')
df = pickle.load(dfPickle)
similarity = pickle.load(similarityPickle)

# Web App
st.title('Job Recommendation System')