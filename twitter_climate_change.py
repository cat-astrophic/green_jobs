# This script uses twint to harvest relevant twitter data

# Importing required modules

import twint
import nest_asyncio
import pandas as pd

# Use nest_asyncio to permit asynchronous loops

nest_asyncio.apply()

# Keywords to search for

keywords = ['globalwarming', 'global warming', 'climatechange', 'climate change']

# Years to search for

years = [y for y in range(2010,2021)]

# Using twint to get data

for y in years:

    # Initializing the annual dataframe
    
    twitter_df = pd.DataFrame()
    
    for k in keywords:
        
        t = twint.Config()
        t.Search = k
        t.Since = str(y) + '-01-01'
        t.Until = str(y) + '-12-31'
        t.Lang = 'en'
        t.Store_csv = True
        t.Pandas = True
        twint.run.Search(t)
        twint.storage.panda.save
        Tweets_df = twint.storage.panda.Tweets_df
        twitter_df = pd.concat([twitter_df, Tweets_df], axis = 0)
    
    # Writing the annual raw data file :: UPDATE USER
    
    twitter_df.to_csv('C:/Users/User/Documents/Data/CC/raw/raw_twitter_data_' + str(y) + '.csv', index = False)

