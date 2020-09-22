import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


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

def replace_dash_with_nan(text):
    '''
    Use with a dataframe column to replace the cell with dash with NaN.
    
    Args:
        text (str) : String of characters.
        
        
    Return:
        revised_text (str) : Text stays the same if value is not a dash; otherwise, function returns NaN.
    
    '''
    if text == '-':
        revised_text = np.NaN
    else:
        revised_text = text
    
    return revised_text
    