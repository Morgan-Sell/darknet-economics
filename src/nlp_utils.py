import pandas as pd
import numpy as np

import re
from bs4 import BeautifulSoup

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def parse_html_remove_url(text):   
    '''
    Parse html and removes internet-related vestige.
    '''
    
    text = BeautifulSoup(text, 'html.parser').get_text().lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'http\S+', '', text)
    return text

def expand_contracted_words(text, contractions_map):
    '''
    Expands contracted words
    '''
    
    text_arr = []
    text = text.split(' ')
    for t in text:
        if t in contractions_map:
            text_arr.append(contractions_map[t])
        else:
            text_arr.append(t)
    
    revised_text = ' '.join(text_arr)
    
    return revised_text


def process_text(text, contractions_map, punc, stopwords, min_len):
    '''
    Prepares text for topic modeling.
    
    '''
    text = parse_html_remove_url(text)
    text = expand_contracted_words(text, contractions_map)
    text = re.sub(r'\w*\d\w*', '', text)
    
    tokens = TweetTokenizer().tokenize(text)
    tokens = [t for t in tokens if t not in punc]
    tokens = [t for t in tokens if t not in stopwords]
    tokens = [t for t in tokens if len(t) >= min_len]
    tokens = [t for t in tokens if t != ' ']
    
    wordnet_lemma = nltk.WordNetLemmatizer()
    lem_tokens = [wordnet_lemma.lemmatize(t) for t in tokens]
    
    return lem_tokens


def bow_vectorizer(docs_raw, min_doc_freq, max_doc_freq, max_feats, ngram_rng):
    '''
    
    Args:
        
    Return:
    
    '''
    vectorizer = CountVectorizer(min_df=min_doc_freq, max_df=max_doc_freq, max_features=max_feats, ngram_range=ngram_rng)
    docs_vectorized = vectorizer.fit_transform(docs_raw)
    return docs_vectorized, vectorizer

def tfidf_vectorizer(docs_raw, min_doc_freq, max_doc_freq, max_feats, ngram_rng):
    '''
    
    Args:
        
    Return:
    
    '''
    vectorizer = TfidfVectorizer(min_df=min_doc_freq, max_df=max_doc_freq, max_features=max_feats, ngram_range=ngram_rng)
    docs_vectorized = vectorizer.fit_transform(docs_raw)
    return docs_vectorized, vectorizer