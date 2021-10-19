#
# Author: Tu Duong
# Date: 10/19/2021
# 
# Simple utility to calculate the asset allocation percentage within the portfolio
# The portfolio can have more than one accounts
# 
# Key columns in the input csv file: Symbol, Current Value
#

import pandas as pd
import argparse


COL_CURRENT_VALUE = 'Current Value'
COL_SYMBOL        = 'Symbol'
COL_QUANTITY      = 'Quantity'
COL_PERCENTAGE    = 'Percentage'


def format_percentage(percentage_value):
    """ Format percentage float value to string
    """
    return("{0:.2f}%".format(percentage_value))


def clean_currency(currency_str):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """

    if isinstance(currency_str, str):
        return(currency_str.replace('$', '').replace(',', ''))

    return(currency_str)
    
        
def main(csv_file):
    """ Main function """

    df = pd.read_csv (csv_file)
    
    # Clean all the rows with Symbol=NaN
    df = df[df[COL_SYMBOL].notna()] 
    
    # Convert currency column from text to float
    df[COL_CURRENT_VALUE] = df[COL_CURRENT_VALUE].apply(clean_currency).astype('float') 
    
    # Group all the rows by Symbol
    grouped_df = df.groupby(COL_SYMBOL).sum()

    # Create Percentage column
    grouped_df['Percentage_Value'] = ( grouped_df[COL_CURRENT_VALUE] / grouped_df[COL_CURRENT_VALUE].sum() ) * 100
    grouped_df['Percentage']       = grouped_df['Percentage_Value'].apply(format_percentage)
    grouped_df.sort_values(by=['Percentage_Value'], inplace=True, ascending=False)

    return(grouped_df)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', help='Full path to the csv file')

    args       = parser.parse_args()
    grouped_df = main(args.csv_file)

    print('----------------------------------------------')
    print(grouped_df[[COL_QUANTITY, COL_CURRENT_VALUE, COL_PERCENTAGE]])
    
    
