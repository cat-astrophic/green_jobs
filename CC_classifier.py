# This script maually classifies select tweets for model training and testing

# This leans heavily on :: https://github.com/gravesa333/Classifying_Climate_Change_Tweets

# Importing required modules

import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score, recall_score
from sklearn.neural_network import MLPClassifier
import seaborn as sns

# Declaring the filepath where the raw data was stored

username = ''
filepath = 'C:/Users/' + username + '/Documents/Data/CC/'

# Initializing the dataframe in which we will store some tweets for manual classification

df = pd.DataFrame()

# Classification lists

believe = ['climatechangeisreal', 'actonclimate', 'extinctionrebellion',
           'climateemergency', 'climateactionnow', 'voteblue']

deny = ['climatechangeisfalse', 'climatechangenotreal', 'climatechangehoax',
        'globalwarminghoax', 'tcot', 'ccot', 'tlot', 'pjnet', 'rednationrising',
        'votered', 'libtard', 'libtards', 'wwg1wga']

# Main loop

for i in range(2010,2021):
    
    print(i) # Visualize progress
    
    d = pd.read_csv(filepath + 'raw/raw_twitter_data_' + str(i) + '.csv') # Read in the raw data
    df = pd.concat([df, d], axis = 0).reset_index(drop = True) # Add to the dataframe
    d = [] # Save space

# Create a classifications column

classifications = [] # Initialize the list

for i in range(len(df)):
    
    print(str(i+1) + ' of ' + str(len(df)) + '.......') # Visualize progress
    
    score = 0
    
    for b in believe:
        
        if b in df.hashtags[i]:
            
            score += 1
                        
    for d in deny:
        
        if d in df.hashtags[i]:
            
            score += -1
            
    if score > 0:
        
        classifications.append('Believer')
        
    elif score < 0:
        
        classifications.append('Denier')
        
    else:
        
        classifications.append(None)

classifications = pd.Series(classifications, name = 'label')
df = pd.concat([df, classifications], axis = 1)

# Subset for only those labelled tweets and indicate via binary the labels

df = df[pd.isnull(df.label) == False].reset_index(drop = True)
score = [1 if l == 'Believer' else 0 for l in list(df.label)]
df = pd.concat([df, pd.Series(score, name = 'score')], axis = 1)
df = df[['tweet', 'score']]

# Split into train and test sets (70/30 ratio)

splitter = np.random.rand(len(df)) < 0.7 # Indices going to training set
train = df[splitter].reset_index(drop = True) # Training set
test = df[~splitter].reset_index(drop = True) # Test set

X_train = train.tweet
Y_train = train.score
X_test = test.tweet
Y_test = test.score

# Data preprocessing for the classifier

def tweet_preprocessor(tweet):
    
    tweet = re.sub('\W+',' ', tweet) # Remove special characters/punctuation
    tweet = tweet.replace('\n', ' ') # Remove line breaks
    tweet = re.sub(r'\bhttps://t.co/\w+', '', tweet) # Remove urls
    tweet = re.sub('\w*\d\w*', ' ', tweet) # Remove numbers
    tweet = tweet.lower() # Convert all text to lowercase
    
    return tweet

lemmatizer = WordNetLemmatizer()

def tweet_tokenizer(tweet):
    
    pretokens = word_tokenize(tweet)
    tokens = [lemmatizer.lemmatize(token) for token in pretokens]
    
    return tokens

new_stop_words = text.ENGLISH_STOP_WORDS.union(believe + deny)

# Build, train, and test the classifier

vectorizer = CountVectorizer(max_df = 0.8, min_df = 3, preprocessor = tweet_preprocessor, tokenizer = tweet_tokenizer, stop_words = new_stop_words)
model = MLPClassifier()

X_train_cv = vectorizer.fit_transform(X_train)
X_test_cv  = vectorizer.transform(X_test)

model.fit(X_train_cv, Y_train)
Y_pred_cv = model.predict(X_test_cv)

# Getting some stats on the training of the model

precision_cv = round(100 * precision_score(Y_test, Y_pred_cv), 3) # 98.128
recall_cv = round(100 * recall_score(Y_test, Y_pred_cv), 3) # 98.506
f1_cv = round(2 * (precision_cv * recall_cv) / (precision_cv + recall_cv), 3) # 98.317

# Creating a confusion matrix

def conf_matrix(actual, predicted):
    
    cm = confusion_matrix(actual, predicted)
    ax = sns.heatmap(cm, xticklabels = ['Predicted Denier', 'Predicted Believer'], 
                yticklabels = ['Actual Denier', 'Actual Beliver'], annot = True,
                fmt='d', annot_kws = {'fontsize':20}, cmap = 'YlGnBu');
    
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom, top)
    true_neg, false_pos = cm[0]
    false_neg, true_pos = cm[1]

    return

conf_matrix(Y_test, Y_pred_cv)

# Read in the geolocated data

ccdata = pd.read_csv(filepath + 'CC_data.csv')

# Transform and run geolcated data through classifier

geotweets = vectorizer.transform(ccdata.tweet)
geoscores = model.predict(geotweets)

# Append results to ccdata and save

geoscores = pd.Series(list(geoscores), name = 'Believer')
ccdata = pd.concat([ccdata, geoscores], axis = 1)
ccdata.to_csv(filepath + 'CC_data.csv', index = False)

