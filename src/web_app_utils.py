import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly

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
    
    file_path = 'C:/Users/morga/OneDrive/Documents/22_Udacity_ML_Nanodegree/darknet-economics/img/daily_posts.html'
    pio.write_html(fig, file=file_path, auto_open=True)
    
    plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
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
    
    wordcloud.to_file('img/wordcloud.jpg')
    
    
def plot_lda_components_distribution(model, vectorizer, model_output, n_topics):
    '''
    Visualizes the number of documents by LDA component.
    
    '''
    sorted_components = np.argsort(model.components_, axis=1)[:, ::-1]
    feat_names = np.array(vectorizer.get_feature_names())

    n_words_per_component = 2

    topics_per_plot = int(n_topics / 2)
    num_docs_per_topic = np.sum(model_output, axis=0)
    barh_xlim = np.max(num_docs_per_topic) * 1.1
    y_arr = np.arange(topics_per_plot)

    topic_names = ['{} {}'.format(i+1, ' '.join(words)) for i, words in enumerate(feat_names[sorted_components[:,:n_words_per_component]])]

    fig = make_subplots(rows=1, cols=2, horizontal_spacing=0.15)
    
    # Plot 1
    n_docs_plot_1 = num_docs_per_topic[:topics_per_plot]

    fig.add_trace(go.Bar(x=n_docs_plot_1[::-1], y=topic_names[:topics_per_plot][::-1], orientation='h'), row=1, col=1)
    fig.update_xaxes(title_text="# of Documents", row=1, col=1)

    # Plot 2
    n_docs_plot_2 = num_docs_per_topic[topics_per_plot:]

    fig.add_trace(go.Bar(x=n_docs_plot_2[::-1], y=topic_names[topics_per_plot:][::-1], orientation='h'), row=1, col=2)
    fig.update_xaxes(title_text="# of Documents", row=1, col=2)

    fig.update_layout(showlegend=False, width=1000, height=800, xaxis=dict(range=[0, barh_xlim]))
    fig.show();