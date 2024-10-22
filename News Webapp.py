#News Webapp
#Making a webapp to get the news I want



import requests
api_key = 'ba7ddf89d7b4455199e4348447b86103'
sources = 'associated-press,ars-technica,bbc-news'

response = requests.get(f'https://newsapi.org/v2/top-headlines?sources={sources}&apiKey={api_key}')
data = response.json()

import pandas as pd
df = pd.DataFrame(data['articles'])

print(df.head())