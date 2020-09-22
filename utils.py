import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import re

def plot_null_val_heatmap(df, plot_title):
    '''
    Identifies null values within a dataframe.
    
    Args:
        df (dataframe) : Dataset to evaluate null values.
        plot_title(str) : Title of heatmap.
    
    Return:
        None
    
    '''
    
    plt.figure(figsize=(25, 10))
    sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
    plt.title(plot_title, fontsize=26, fontweight='bold')
    plt.tight_layout();
    
    
def convert_price_to_float(price):
    '''
    Transforms price, which may be a string object, to a float object.
    
    Args:
        price (str) : Price is expected to start w/ a "$".
    
    Returns:
        adj_price (float) : Float object to be used for calculations/modelinng.
    
    '''

    if price == '-':
        adj_price = np.NaN
        
    elif type(price) == float:
        adj_price = price
        
    elif type(price) == str:
        tmp = price.replace('$', '')
        adj_price = tmp.replace(',', '')
        adj_price = float(adj_price)
    
    return adj_price


def stats_summary(arr):
    '''
    Basic stats summary.
    
    Args:
        arr (arr) : Array of numeric values.
    
    Returns:
        None
    
    '''
    print('STATS SUMMARY:')
    print('Mean: ', arr.mean())
    print('Median: ', arr.median())
    print('Std. Dev.: ', arr.std())
    print('Max value: ', arr.max())
    print('Min value: ', arr.min())
    print('# of Obs.: ', len(arr))

def replace_empty_cell_with_nan(text):
    '''
    Use with a dataframe column to replace an empty cell with dash with NaN.
    
    Args:
        text (str) : String of characters.
        
    Return:
        revised_text (str) : If cell is empty then returns NaN; otherwise, returns intial text.
    
    '''
    if text == '':
        revised_text = np.NaN
   
    else:
        revised_text = text
    
    return revised_text

def replace_split_text(text, re_chars, replacement):
    '''
    Remove unecessary characters and transformed text into a list. 
    
    Args:
        text (str) : String of characters.
        re_chars (str) : Input in regex format.
        replacement (str) : String used to replace
        
    Return:
        revised_text (arr) : Cleaned text in a list.
    
    '''
    # regex_conversion = 'r'+
    revised_text = re.sub(re_chars, replacement, str(text))
    revised_text = re.split('\s+', revised_text)
    return revised_text[1:]