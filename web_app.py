import pandas as pd
import numpy as np

import streamlit as st
import pydeck as pdk

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src import web_app_utils


MASTER_DATA_URL = (
    "https://darknet-market-forums-udacity-capstone.notebook.us-west-2.sagemaker.aws/edit/darknet-economics/data/wallstreet_master.csv"
)

SENTIMENT_DATA_URL = (
    "https://darknet-market-forums-udacity-capstone.notebook.us-west-2.sagemaker.aws/files/darknet-economics/data/sentiment_analysis_data.csv?_xsrf=xsrf-token-set-by-sagemaker-1602265257458"
)


st.title("What's Trending in the Opaque Corners on the Internet?")
st.markdown("Topic Modeling and Sentiment Analysis of Wall Street Market Forum")

# prevents calculation from being performed everytime the app is reran.
@st.cache(persist=True)
def load_data(data_url):
    data = pd.read_csv(data_url)
    return data

wallstreet = load_data(MASTER_DATA_URL)
sentiment = load_data(SENTIMENT_DATA_URL)

# Line chart showing the number of daily forum posts.
st.header('Number of Daily Forum Posts')
web_app_utils.plot_daily_post_freq(wallstreet['post_date'])


# Wordcloud
st.header('Word Frequency throughout All Posts')
max_words = st.slider('Select the maximum number of words to display.', 100, 10000)

grouped_text = st.checkbox("Include grouped text")

if grouped_text:
    show_grouped_text = True
else:
    show_grouped_text = False
    
web_app_utils.display_wordcloud(wallstreet['cleaned_post'], max_words, show_grouped_text)


# Sentment Time-Series Analysis

st.header('Wall Street Forum Sentiment Time-Series Analysis')
st.markdown("Uses VADER")
sentiment_option = (label='Which metrics would you like to evaulate?',
                   options=('Lifetime Avg', 'Lifetime Median', 'Lifetime Innerquartile Range', 'Daily Avg',
                    'Daily Median', 'Daily Min/Max'))
st.line_chart(sentiment[sentiment_option])