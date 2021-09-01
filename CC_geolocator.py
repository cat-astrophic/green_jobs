# This script subsets the raw data for tweets with geolocation data

# Importing required modules

import pandas as pd

# Declaring the filepath where the raw data was stored

username = ''
filepath = 'C:/Users/' + username + '/Documents/Data/CC/'

# Initializing a dataframe which will hold the tweets with geolocation data

geodf = pd.DataFrame()

# Main loop

for year in range(2010,2021):
    
    print('Year == ' + str(year) + '.......')
    df = pd.read_csv(filepath + 'raw/raw_twitter_data_' + str(year) + '.csv') # Read in the raw data
    df = df[pd.isnull(df.place) == False] # Subset for non Null geolocation data
    geodf = pd.concat([geodf, df], axis = 0) # Append to main dataframe
    
# Write the geolocation dataframe to file

geodf.to_csv(filepath + 'CC_data.csv', index = False)

