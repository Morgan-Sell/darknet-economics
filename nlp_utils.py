import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import re

from bs4 import BeautifulSoup

import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def clean_parse_text(text):
    '''
   
    Args:
        
        
    Return:
        
    '''
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'\n', ' ', text)
    cleaned_text = re.sub(r'[^a-zA-Z0-9$!?.]', ' ', text)
    return cleaned_text

def clean_tokenize_lemmatize(text):
    '''
    Removes HTML tags and stopwords.
    Converts words to its base using lemmatization.
    
    
    Args:
        comment (str) : Content of the author's post in Wall Street Market.
        
    Return:
        lem_tokens (arr) : The cleaned, tokenized and lemmetized version of comment.
        
    '''
    
    cleaned_text = clean_parse_text(text)
    
    tokens = nltk.word_tokenize(cleaned_text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    
    wordnet_lemma = nltk.WordNetLemmatizer()
    lem_tokens = [wordnet_lemma.lemmatize(t) for t in tokens]
    
    return lem_tokens

def print_topics(topics, feature_names, sorting, topics_per_chunk=6, n_words=20):
    for i in range(0, len(topics), topics_per_chunk):
        # for each chunk:
        these_topics = topics[i: i + topics_per_chunk]
        # maybe we have less than topics_per_chunk left
        len_this_chunk = len(these_topics)
        # print topic headers
        print(("topic {:<8}" * len_this_chunk).format(*these_topics))
        print(("-------- {0:<5}" * len_this_chunk).format(""))
        # print top n_words frequent words
        for i in range(n_words):
            try:
                print(("{:<14}" * len_this_chunk).format(
                    *feature_names[sorting[these_topics, i]]))
            except:
                pass
        print("\n")