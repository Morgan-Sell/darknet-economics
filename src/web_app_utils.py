import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

from wordcloud import WordCloud


def plot_daily_post_freq(series):
    '''
    Interactive line plot showing the number of plots per day.
    '''
    daily_post_freq = pd.DataFrame(series.value_counts()).reset_index()
    daily_post_freq.columns = ['date', 'count']
    daily_post_freq.sort_values(['date'], axis=0, inplace=True)
    fig = px.line(data_frame=daily_post_freq, x='date', y='count',
                  labels={'date': 'Date', 'count': '# of Posts'})
    fig.update_layout(width=1500, height=600)
    fig.show()

def display_wordcloud(pd_series, max_words, grouped_text):
    '''
    Generates wordcloud.
    '''

    series_as_str = pd_series.astype('str')
    joined_wordcloud_text = ' '.join(series_as_str)

    wordcloud = WordCloud(background_color='white', max_words=max_words, contour_color='steelblue', collocations=grouped_text)
    wordcloud.generate(joined_wordcloud_text)

    plt.figure(figsize=(20,7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off');