import streamlit as st
import pandas as pd
# import pickle

dfPickle = open("../Backend/df.pkl", 'rb')
similarityPickle = open("../Backend/similarity.pkl", 'rb')
df = pd.read_pickle(dfPickle)
similarity = pd.read_pickle(similarityPickle)


def recommendation(title):
    placeIndex = df[df['Title'] == title].index[0]
    placeIndex = df.index.get_loc(placeIndex)
    distances = sorted(list(enumerate(similarity[placeIndex])),key=lambda x: x[1], reverse=False)[1:20]
    
    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)
    return jobs

# Web App
st.title('Job Recommendation System')
title = st.selectbox('search job', df['Title'])
jobs = recommendation(title)

if jobs:
    st.write(jobs)