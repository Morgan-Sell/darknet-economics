import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
# plotly.express enables the quick creation of interactive plots assuming data
# is in well-organized dataframes.
import plotly.express as px

from src import dashboard_utils










st.header('Word Frequency throughout All Posts')

max_words = st.slider('Select the maximum number of words to display.', 100, 10000)
