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

def clean_and_split_text(text, re_chars, replacement):
    '''
    Remove unecessary characters and transformed text into a list. 
    
    Args:
        text (str) : String of characters.
        re_chars (str) : Input in regex format.
        replacement (str) : String used to replace
        
    Return:
        revised_text (arr) : Cleaned text in a list.
    
    '''
    
    revised_text = re.sub(r'\t', '', str(text))
    revised_text = re.sub(r'\n', '', str(revised_text))
    revised_text = re.sub(re_chars, replacement, revised_text)
    revised_text = re.split('\s+', revised_text)
    return revised_text[1:]

def aggregate_categories_to_master_groups(category):
    '''
    Summarizes products into master products
    
    Args:
        text (str) : String of characters.
        re_chars (str) : Input in regex format.
        replacement (str) : String used to replace
        
    Return:
        revised_text (arr) : Cleaned text in a list.
    
    '''
    illicit_keywords = ['Psychedelics', 'Ecstacy']
    cannibis_keywords = ['Cannibis',]
    otc_keywords = ['Opioids', 'Prescription', 'Benzos', 'Opiods']
    fraud_security_goods_keywords = ['Fraud', 'Security']
    security_services_keywords = ['Hacking']

    
    
def create_product_id(seq, num_ints, year):
    '''
    Creates a product id by merging the initial sequence number or product id with the year the product was offered.
    Adds zeros to the front of the "seq" value to ensure number of integers.
    
    Args:
        seq (int) : A sequence of numbers.
        num_int (int) : number of integer in the product id excluding the year.
        year (int) : Four digits.
        
    Return:
        product_id (str) : Identifier for the product. Format is "yy-nnnnnn". Number of digits ("n") can vary.
    
    '''
    
    seq_str = str(int(seq)).zfill(num_ints)
    year_str = str(year)[2:]
    product_id = year_str + '-' + seq_str
    return product_id

def select_non_null_value(x, y):
    '''
    Returns the non-null value. 
    If neither value is null, returns x.
    
    Args:
        x (float) : Float or
        y (float) : number of integer in the product id excluding the year.
         
    Return:
        res : Non-null value
    '''
    
    if not np.isnan(x):
        res = x
    else:
        res = y
    return res