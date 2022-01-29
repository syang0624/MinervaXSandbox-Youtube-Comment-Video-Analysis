import os
import pandas as pd # pandas for data manipulation + data analysis
import numpy as np # numpy for math
import matplotlib.pyplot as plt # pyplot for visualization
import datetime # datetime for computing times
import seaborn as sns #seaborn for visualization
import statsmodels.api as statsmodels # for regression
from scipy import stats # more regression 
from sklearn import linear_model # regression model
from pylab import rcParams
rcParams['figure.figsize'] = 15, 8 # set figsize for all plots

# Load json dataset into pandas dataframe
df = pd.read_json("thumbnail_and_sound_analysis.json")

# remove unnecessary columns
df = df.drop(columns=['channel_id', 'status', 'game_tag', 'is_paid', 'is_music_claim', 
                      'description', 'title', 'published_at'])
df.head()

# !pip install --upgrade google-api-python-client
# !pip install --upgrade google-auth-oauthlib google-auth-httplib2
from googleapiclient.discovery import build

def get_stats(video_id):
    
    # create youtube resource object
    youtube = build("youtube", "v3", developerKey = "AIzaSyDsD5jELu-4jyFRYpeUfOiueSuuBMXz7aA")
    
    # get the video statistics
    request = youtube.videos().list(part='statistics', id=video_id)
    response = request.execute()
    
    # return None if request has no result, e.g. private video
    if not response['items']:
        return None
    
    items = response['items'][0]
    
    viewCount = items['statistics']['viewCount']
    likeCount = items['statistics']['likeCount']
    dislikeCount = items['statistics']['dislikeCount']
    favoriteCount = items['statistics']['favoriteCount']
    commentCount = items['statistics']['commentCount']
    
    return viewCount, likeCount, dislikeCount, favoriteCount, commentCount

def add_apidata(df):
    
    for index, row in df.iterrows():
        stats = get_stats(row["video_id"])
        
        if stats is None:
            df.loc[index, 'view_count'] = None
            df.loc[index, 'like_count'] = None
            df.loc[index, 'dislike_count'] = None
            df.loc[index, 'favorite_count'] = None
            df.loc[index, 'comment_count'] = None
        
        else:
            df.loc[index, 'view_count'] = stats[0]
            df.loc[index, 'like_count'] = stats[1]
            df.loc[index, 'dislike_count'] = stats[2]
            df.loc[index, 'favorite_count'] = stats[3]
            df.loc[index, 'comment_count'] = stats[4]

    return df

add_apidata(df).head()