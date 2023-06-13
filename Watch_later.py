#!/usr/bin/env python
# coding: utf-8

# In[84]:


pip install --upgrade google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2


# In[96]:


get_ipython().system('pip install isodate')


# In[97]:


import isodate
import pandas as pd


# In[98]:


import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

wl = pd.read_csv("./Watch later.csv")
# Set the video ID for the video you want to get the duration for
vid_ids = wl['Playlist Id'][2:]
# vid_ids = wl[0][2:]
# print(vid_ids)

vid_ids

api_key = "Put your API key here"


# In[99]:


name = []
length = []
link = []

youtube = build("youtube", "v3", developerKey=api_key)

for video in vid_ids:
    response = youtube.videos().list(part="contentDetails", id=video).execute()
    if(len(response['items']) == 0):
        continue
    response2 = youtube.videos().list(part="snippet", id=video).execute()
    if(len(response2['items']) == 0):
        continue
# Parse the duration value from the API response
    title = response2["items"][0]["snippet"]["title"]
    duration = response["items"][0]["contentDetails"]["duration"]
    name.append(title)
    
    duration = isodate.parse_duration(duration)
    duration_minutes = duration.total_seconds() / 60

    length.append(duration_minutes)
    link.append("https://youtu.be/"+video)
# Convert the timedelta to minutes
    


ans = pd.DataFrame()
ans['Title'] = name
ans['Duration'] = length
ans['URL'] = link
ans = ans.sort_values(by=['Duration'])
  
ans.to_csv('watch_later_sorted.csv', index=False)






