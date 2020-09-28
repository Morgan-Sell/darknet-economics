import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import re

from bs4 import BeautifulSoup

import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def clean_parse_text(text):
    '''
   
    Args:
        
        
    Return:
        
    '''
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'\n', ' ', text)
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
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
    tokens = [t.lower() for t in tokens]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    
    wordnet_lemma = nltk.WordNetLemmatizer()
    lem_tokens = [wordnet_lemma.lemmatize(t) for t in tokens]
    
    return lem_tokens


def print_topics(model, count_vectorizer, n_top_words):
    '''
   
    Args:
    
        
    Return:
    
        
    '''
    
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        top_words_arr = [words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        print("\nTopic #{}:".format(topic_idx))
        print(" ".join(top_words_arr))

        
def convert_to_bow_and_fit_lda_model(docs_raw, max_feats, freq_thresh, n_topics, learning_method, max_iter, random_state=3):
    '''
    Convert text into a vector representation, i.e. Bag of Words.
    
    Args:
        docs_raw (arr) : An array comprised of numerous texts.
        max_feats (int) : Number of words to limit the bag-of-words.
        freq-thresh (float) : Words that have a document frequency greater than the selected amount will be ignored.
    Return:
        text_transformed (arr) : Vectorized texted.
    
    '''
    
    vect = CountVectorizer(max_features=max_feats, max_df=freq_thresh)
    docs_transformed = vect.fit_transform(docs_raw)

    lda = LatentDirichletAllocation(n_components=n_topics, learning_method=learning_method, max_iter=max_iter, random_state=random_state, n_jobs=-1)
    doc_topics = lda.fit_transform(docs_transformed)
    
    return doc_topics, lda, vect


def calculate_tfidf_and_fit_lda_model(docs_raw, max_feats, freq_thresh, n_topics, learning_method, max_iter, random_state=3):
    '''
    Convert text into a vector representation, i.e. Bag of Words.
    
    Args:
        docs_raw (arr) : An array comprised of numerous texts.
        max_feats (int) : Number of words to limit the bag-of-words.
        freq-thresh (float) : Words that have a document frequency greater than the selected amount will be ignored.
    Return:
        text_transformed (arr) : Vectorized texted.
    
    '''
    
    vect = TfidfVectorizer(max_features=max_feats, max_df=freq_thresh)
    docs_transformed = vect.fit_transform(docs_raw)

    lda = LatentDirichletAllocation(n_components=n_topics, learning_method=learning_method, max_iter=max_iter, random_state=random_state, n_jobs=-1)
    doc_topics = lda.fit_transform(docs_transformed)
    
    return doc_topics, lda, vect

def print_topics(model, count_vectorizer, n_top_words):
    '''
    
    Args:
        
    Return:
        
    '''
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        top_words_arr = [words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        print("\nTopic #{}:".format(topic_idx))
        print(" ".join(top_words_arr))
        
        