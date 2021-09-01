# This script creates county level values from the CC_data file using geopy
# Importing required modules

import pandas as pd
from geopy.geocoders import Nominatim

# Declaring username + filepath

username = ''
filepath = 'C:/Users/' + username + '/Documents/Data/CC/'

# Reading in the tweets data

ccdata = pd.read_csv(filepath + 'CC_data.csv')

# Creating a more concise, usable data set

b = []
lat = []
long = []

for i in range(len(ccdata)):
    
    b.append(ccdata.Believer[i])
    s = ccdata.place[i]
    s = s[34:len(s)-2]
    idx = s.find(',')
    lat.append(s[:idx])
    long.append(s[idx+2:])

b = pd.Series(b, name = 'Believer')
lat = pd.Series(lat, name = 'lat')
long = pd.Series(long, name = 'long')
df = pd.concat([b, lat, long], axis = 1)

# Determining the source of each tweet

# Defining the geolocator

geolocator = Nominatim(user_agent = 'geoapiExercises')

# Using geolocator for each observation

locations = []

for i in range(len(df)):
    
    print('Getting address of tweet ' + str(i+1) + ' of ' + str(len(df)) + '.......') # Visualize progress
    
    try:
        
        locations.append(geolocator.reverse(df.lat[i] + ',' + df.long[i]))
        
    except:
        
        locations.append(None)

# Determining which tweets are from the US and adding this info to the df

us = []
counties = []
states = []
city = []
printval = 0

for l in locations:
    
    printval += 1 # This will make printing the progress tracker faster than calling .index()
    print('Is tweet ' + str(printval) + ' of ' + str(len(locations)) + ' in the US?') # Visualize progress
    
    try:
            
        a = l.raw['address']
        
        try:
            
            if a['country'] == 'United States':
                
                try:
                    
                    counties.append(a['county'])
                    city.append(0)
                    us.append(1)
                    states.append(a['state'])
                    
                except:
                    
                    try:
                        
                        counties.append(a['city'])
                        city.append(1)
                        us.append(1)
                        states.append(a['state'])
                        
                    except:
                        
                        counties.append(a['town'])
                        city.append(1)
                        us.append(1)
                        states.append(a['state'])
                
            else:
                
                us.append(0)
                counties.append(None)
                states.append(None)
                city.append(0)
                
        except:
            
            us.append(0)
            counties.append(None)
            states.append(None)
            city.append(0)
        
    except:
        
        us.append(0)
        counties.append(None)
        states.append(None)
        city.append(0)

us = pd.Series(us, name = 'US')
counties = pd.Series(counties, name = 'County')
states = pd.Series(states, name = 'State')
city = pd.Series(city, name = 'City')
df = pd.concat([df, us, counties, states, city], axis = 1)

##### 143,014 of 273,211 tweets with geolocation data came from the US

# Subset for tweets prior to 2016

def get_year(inp):
    
    s1 = inp.find('/')
    inp = inp[s1+1:]
    s2 = inp.find('/')
    inp = inp[s2+1:]
    year = int(inp[:4])
    
    return year

years = [get_year(ccdata.date[i]) for i in range(len(ccdata))]
sample = [int(y < 2016) for y in years]
years = pd.Series(years, name = 'Year')
sample = pd.Series(sample, name = 'Sample')
df = pd.concat([df, years, sample], axis = 1)

# Write df to file

df.to_csv(filepath + 'county_data_raw.csv', index = False)

