#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:57:14 2021

@author: tlo
"""
import json
import pandas as pd
#import nltk 
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

# saves a str of the path of the messages folder
path_to_file = '/Users/tlo/code/facebook chat logs/facebook chat/facebook-tadosalvo (2)/messages/inbox/teamslaggagoonsquad_h8lzsvkjrg/message_1.json'

# opens file as file and loads the data and saves in chat history variable
with open(path_to_file) as file:
    chat_history = json.load(file)


# prints out keys in dictionary
chat_history.keys()

# prints out only the messages section of the json file
#print(chat_history['messages'])

messages = pd.DataFrame(chat_history['messages'])


#print(messages)

# uses pandas datetime function to convert
def convert_time(timestamp):
    return pd.to_datetime(timestamp,unit = 'ms')

#print(convert_time(1624560771767))

# applys convert time function to timestamp_ms
messages['date'] = messages['timestamp_ms'].apply(convert_time)



def get_month(date):
    return date.month

def get_year(date):
    return date.year

messages['month'] = messages['date'].apply(get_month)
messages['year'] = messages['date'].apply(get_year)

#print(messages)

def get_lower(content):
    return content.lower()

messages['content'] = messages['content'].astype(str)

messages['content_lower'] = messages['content'].apply(get_lower)




