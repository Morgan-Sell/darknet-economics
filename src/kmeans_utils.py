import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import IncrementalPCA

from scipy.spatial.distance import cdist

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_distortion_inertia(k_rng, distortions, inertias):
    '''
    Use plots to determine optimal number of clusters.
    '''
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Distortion', 'Inertia'))

    fig.add_trace(go.Scatter(x=k_rng, y=distortions), row=1, col=1)
    fig.update_xaxes(title_text="# of Clusters", row=1, col=1)
    fig.update_yaxes(title_text="Average of Squared Errors", row=1, col=1)

    fig.add_trace(go.Scatter(x=k_rng, y=inertias), row=1, col=2)
    fig.update_xaxes(title_text="# of Clusters", row=1, col=2)
    fig.update_yaxes(title_text="Sum of Squared Errors", row=1, col=2)

    fig.update_layout(showlegend=False)
    for i in fig['layout']['annotations']:
        i['font'] = dict(size=26)

    file_path = 'C:/Users/morga/OneDrive/Documents/22_Udacity_ML_Nanodegree/darknet-economics/img/plot_distortion_inertia.jpg'
    fig.write_image(file_path)
    
    fig.show();
    
    