import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF

from gensim.models.coherencemodel import CoherenceModel
from gensim.corpora.dictionary import Dictionary
from gensim.models.nmf import Nmf

import matplotlib.pyplot as plt


def create_gensim_dict_corpus(docs_raw, num_below, num_above, num_features):
    '''
    Create corpus to be used to determine optimal number of components using the gensim package.
    
    '''
    gensim_dict = Dictionary(docs_raw)
    gensim_dict.filter_extremes(no_below=num_below, no_above=num_above, keep_n=num_features)
    corpus = [gensim_dict.doc2bow(doc) for doc in docs_raw]
    
    return gensim_dict, corpus

def plot_coherence_scores(num_topics_rng, scores):
    '''
    Visualize coherence scores for their respective number of topics.
    Use to determine optimal number of topics for sklearn NMF model.
    '''
    
    coherence_scores = [scores[i][1] for i in range(len(scores))]

    fig, ax = plt.subplots(figsize=(9,5))
    ax.plot(num_topics_rng, coherence_scores, linewidth=3)
    ax.set_title('NMF Model Performance by Number of Topics', fontsize=14)
    ax.set_xlabel('# of Topics')
    ax.set_ylabel('Coherence Score')
    plt.tight_layout();