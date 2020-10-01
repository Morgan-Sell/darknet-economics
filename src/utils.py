import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import re

from datetime import datetime

def plot_null_val_heatmap(df, plot_title, figsize):
    '''
    Identifies null values within a dataframe.
    
    Args:
        df (dataframe) : Dataset to evaluate null values.
        plot_title(str) : Title of heatmap.
        figsize (tuple) : Plot dimensions
    
    Return:
        None
    
    '''
    
    plt.figure(figsize=figsize)
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
    return revised_text


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

def fix_postdate_col(dt):
    '''
    The last 2 days have errors in the dates.
    This function resolves the errors.
    
    Args:
        dt (str) : date and time
    Returns:
        dt_revised (datetime) : date and time
    
    '''
    dt_split = dt.split(' ')
    date = dt_split[0]
    time = dt_split[1]
    
    if date == 'Yesterday':
        date = '2018-11-13'
    
    elif date == 'Today':
        date = '2018-11-14'
    
    dt_merged = date + ' ' + time
    dt_revised = datetime.strptime(dt_merged, '%Y-%m-%d %H:%M:%S')
    
    return dt_revised


def fix_author_join_date_col(join_date, author_membership, post_date):
    '''
    If a date is not in the value, function develops an assumption.
    
    Args:
        join_date (str) : Value for which the author is assumed to have joined.
        author_memberhsip (str) : Author's Wall Street membership level.
        post_date (datetime) : Date and time the author posted the corresponding comment.
        mode_date (str) : Most common date in the relavant data series.
        
    Returns:
        join_date_revised (datetime) : date 
    '''
    
    try:
        join_date_revised = datetime.strptime(join_date, '%Y-%m-%d')

    except:
        if author_membership == 'New member':
            join_date_revised = post_date.date()
        else:
            join_date_revised = np.nan
    
    return join_date_revised
    