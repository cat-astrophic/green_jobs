# This script creates county mean values for the CC belief data set

# Importing required modules

import pandas as pd

# Declaring the filepath where the raw data was stored

username = ''
filepath = 'C:/Users/' + username + '/Documents/Data/CC/'

# Reading in the data

data = pd.read_csv(filepath + 'county_data_raw.csv')

# Dropping those tweets not in the sample

data = data[data.Sample == 1].reset_index(drop = True)
data = data[data.US == 1].reset_index(drop = True)

# Rename certain counties so that they can eventually be assigned FIPS codes

county = list(data.County)
state = list(data.State)
city = list(data.City)

for i in range(len(county)):
    
    print('Checking county ' + str(i+1) + ' of ' + str(len(data)) + '.......') # Visualize progress
    
    if state[i] == 'California' and city[i] == 1:
        
        county[i] = 'Los Angeles County'
        
    elif state[i] == 'District of Columbia':
        
        county[i] = 'District of Columbia'
        
    elif state[i] == 'Illinois' and city[i] == 1:
        
        county[i] = 'Cook County'
        
    elif state[i] == 'Indiana' and county[i] == 'Indianapolis':
        
        county[i] = 'Marion County'
        
    elif state[i] == 'Indiana' and county[i] == 'Clarksville':
        
        county[i] = 'Clark County'
        
    elif state[i] == 'Indiana' and county[i] == 'Jeffersonville':
        
        county[i] = 'Clark County'
        
    elif state[i] == 'Maine' and city[i] == 1:
        
        county[i] = 'Somerset County'
        
    elif state[i] == 'Maryland' and city[i] == 1:
        
        county[i] = 'Baltimore city'
        
    elif state[i] == 'Missouri' and city[i] == 1:
        
        county[i] = 'St. Louis city'
        
    elif state[i] == 'New Jersey' and county[i] == 'New York County':
        
        state[i] = 'New York'
        
    elif state[i] == 'New York' and city[i] == 1:
        
        county[i] = 'New York County'
        
    elif state[i] == 'Pennsylvania' and city[i] == 1:
        
        county[i] = 'Susquehanna County'
        
    elif state[i] == 'Washington' and county[i] == 'Omak':
        
        county[i] = 'Okanogan County'
        
    elif state[i] == 'Missouri' and city[i] == 1:
        
        county[i] = 'St. Louis city'
        
    elif state[i] == 'Connecticut' and county[i] == 'Worcester County':
        
        state[i] = 'Massachusetts'
        
    elif state[i] == 'South Carolina' and county[i] == 'Robeson County':
        
        state[i] = 'North Carolina'
        
    elif state[i] == 'Alaska' and county[i] == 'Anchorage':
    
        county[i] = 'Anchorage Municipality'
    
    elif state[i] == 'Alaska' and county[i] == 'Denali':
    
        county[i] = 'Denali Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Fairbanks North Star':
    
        county[i] = 'Fairbanks North Star Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Juneau':
    
        county[i] = 'Juneau City and Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Kenai Peninsula':
    
        county[i] = 'Kenai Peninsula Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Ketchikan Gateway':
    
        county[i] = 'Ketchikan Gateway Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Kodiak Island':
    
        county[i] = 'Kodiak Island Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Matanuska-Susitna':
    
        county[i] = 'Matanuska-Susitna Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Nome':
    
        county[i] = 'Nome Census Area'
    
    elif state[i] == 'Alaska' and county[i] == 'North Slope':
    
        county[i] = 'North Slope Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Northwest Arctic':
    
        county[i] = 'Northwest Arctic Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Petersburg Borough':
    
        county[i] = 'Petersburg Census Area'
    
    elif state[i] == 'Alaska' and county[i] == 'Sitka':
    
        county[i] = 'Sitka City and Borough'
    
    elif state[i] == 'Alaska' and county[i] == 'Skagway':
    
        county[i] = 'Skagway Municipality'
    
    elif state[i] == 'Alaska' and county[i] == 'Yakutat':
    
        county[i] = 'Yakutat City and Borough'
    
    elif state[i] == 'California' and county[i] == 'San Francisco':
    
        county[i] = 'San Francisco County'
    
    elif state[i] == 'Colorado' and county[i] == 'City and County of Broomfield':
    
        county[i] = 'Broomfield County'
    
    elif state[i] == 'Georgia' and county[i] == 'Athens-Clarke County':
    
        county[i] = 'Clarke County'
    
    elif state[i] == 'Hawaii' and county[i] == 'HawaiÊ»i County':
    
        county[i] = 'Hawaii County'
    
    elif state[i] == 'Hawaii' and county[i] == 'KauaÊ»i County':
    
        county[i] = 'Kauai County'
    
    elif state[i] == 'Illinois' and county[i] == 'DeWitt County':
    
        county[i] = 'De Witt County'
    
    elif state[i] == 'Illinois' and county[i] == 'Saint Clair County':
    
        county[i] = 'St. Clair County'
    
    elif state[i] == 'Indiana' and county[i] == 'Floyd':
    
        county[i] = 'Floyd County'
    
    elif state[i] == 'Indiana' and county[i] == 'Jefferson':
    
        county[i] = 'Jefferson County'
    
    elif state[i] == 'Indiana' and county[i] == 'Marion':
    
        county[i] = 'Marion County'
    
    elif state[i] == 'Indiana' and county[i] == 'Monroe':
    
        county[i] = 'Monroe County'
    
    elif state[i] == 'Indiana' and county[i] == 'Porter':
    
        county[i] = 'Porter County'
    
    elif state[i] == 'Indiana' and county[i] == 'Saint Joseph County':
    
        county[i] = 'St. Joseph County'
    
    elif state[i] == 'Louisiana' and county[i] == 'Saint Bernard Parish':
    
        county[i] = 'St. Bernard Parish'
    
    elif state[i] == 'Louisiana' and county[i] == 'Saint Helena Parish':
    
        county[i] = 'St. Helena Parish'
    
    elif state[i] == 'Maryland' and county[i] == "Saint Mary's County":
    
        county[i] = "St. Mary's County"
    
    elif state[i] == 'Michigan' and county[i] == 'Saint Clair County':
    
        county[i] = 'St. Clair County'
    
    elif state[i] == 'Michigan' and county[i] == 'Saint Joseph County':
    
        county[i] = 'St. Joseph County'
    
    elif state[i] == 'Minnesota' and county[i] == 'Saint Louis County':
    
        county[i] = 'St. Louis County'
    
    elif state[i] == 'Missouri' and county[i] == 'Saint Charles County':
    
        county[i] = 'St. Charles County'
    
    elif state[i] == 'Missouri' and county[i] == 'Saint Louis County':
    
        county[i] = 'St. Louis County'
    
    elif state[i] == 'Missouri' and county[i] == 'Sainte Genevieve County':
    
        county[i] = 'Ste. Genevieve County'
    
    elif state[i] == 'New Mexico' and county[i] == 'DoÃ±a Ana County':
    
        county[i] = 'Do√±a Ana County'
    
    elif state[i] == 'New York' and county[i] == 'Saint Lawrence County':
    
        county[i] = 'St. Lawrence County'
    
    elif state[i] == 'Rhode Island' and county[i] == 'South County':
    
        county[i] = 'Washington County'
    
    elif state[i] == 'Virginia' and county[i] == 'Alexandria':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Arlington':
    
        county[i] = county[i] + ' County'
    
    elif state[i] == 'Virginia' and county[i] == 'Bristol':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Charlottesville':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Chesapeake':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Colonial Heights':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Danville':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Fairfax (city)':
    
        county[i] = 'Fairfax city'
    
    elif state[i] == 'Virginia' and county[i] == 'Falls Church':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Fredericksburg':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Hampton':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Harrisonburg':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Hopewell':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Lexington':
    
        county[i] = county[i] + ' city'
        
    elif state[i] == 'Virginia' and county[i] == 'Lynchburg':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Manassas':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Manassas Park':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Martinsville':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Newport News':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Norfolk':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Petersburg':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Poquoson':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Portsmouth':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Radford (city)':
    
        county[i] = 'Radford city'
    
    elif state[i] == 'Virginia' and county[i] == 'Richmond':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Roanoke':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Salem':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Staunton':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Suffolk':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Suffolk (city)':
    
        county[i] = 'Suffolk city'
    
    elif state[i] == 'Virginia' and county[i] == 'Virginia Beach':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Waynesboro':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Virginia' and county[i] == 'Williamsburg (city)':
    
        county[i] = 'Williamsburg city'
    
    elif state[i] == 'Virginia' and county[i] == 'Winchester':
    
        county[i] = county[i] + ' city'
    
    elif state[i] == 'Washington' and county[i] == 'Okanogan':
    
        county[i] = 'Okanogan County'
    
    elif state[i] == 'Wisconsin' and county[i] == 'Saint Croix County':
    
        county[i] = 'St. Croix County'

# Replacing these three columns in data

data = data[[col for col in data.columns if col not in ['City', 'County', 'State']]]
data = pd.concat([data, pd.Series(county, name = 'County'), pd.Series(state, name = 'State')], axis = 1)

# Creating an ID for groupby and adding to data

uid = [str(data.County[i]) + str(data.State[i]) for i in range(len(data))]
data = pd.concat([data, pd.Series(uid, name = 'ID')], axis = 1)

# Creating county level data

df = data.groupby(['ID']).mean() # Get mean values
df = df[[col for col in df.columns if col in ['Believer', 'City']]] # Keep mean belief data + city indicator

df2 = data.groupby(['ID']).count() # Get counts
df = pd.concat([df, df2['Sample']], axis = 1) # Add counts to df

# Parse IDs and add county and state to df

counties = [list(data.County)[uid.index(x)] for x in list(df.index)]
states = [list(data.State)[uid.index(x)] for x in list(df.index)]
df = df.reset_index(drop = True) # So that indices will match for merge
df = pd.concat([df, pd.Series(counties, name = 'County'), pd.Series(states, name = 'State')], axis = 1)

# Loading a data set used for mapping city, state to county, state for such instances

fipdf = pd.read_csv(filepath + 'county_fips.csv')

# Adding an ID column to fipdf

fipids = [str(fipdf.stname[i]) + str(fipdf.ctyname[i]) for i in range(len(fipdf))]
fipdf = pd.concat([fipdf, pd.Series(fipids, name = 'ID')], axis = 1 )

# A function to help get fips from fipdf

def fips_fxn(inp):
    
    try:
        
        idx = fipdf.index[fipdf.ID == inp][0]
        f = fipdf.fips[idx]
        
    except:
        
        f = None
    
    return f

# Adding FIPS to df

dfID = [str(df.State[i]) + str(df.County[i]) for i in range(len(df))]
fips = [fips_fxn(x) for x in dfID]
df = pd.concat([df, pd.Series(fips, name = 'FIPS')], axis = 1)

# Drop non US state data

df = df[~df.State.isin(['Puerto Rico', 'Guam', 'American Samoa', 'Northern Mariana Islands', 'United States Virgin Islands'])].reset_index(drop = True)
df = df[~df.County.isin(['nan', 'Unorganized Borough'])].reset_index(drop = True)

# Manually adding FIPS codes for three counties with special characters in names (two in HI, one in NM)

dfips = list(df.FIPS)
dfips[584] = 35013
dfips[847] = 15001
dfips[1015] = 15007
addfips = [int(f) for f in dfips]
df = df.drop(['FIPS'], axis = 1)
df = pd.concat([df, pd.Series(addfips, name = 'FIPS')], axis = 1)

# Save df as csv

df.to_csv(filepath + 'county_data.csv', index = False)

