
from googleapiclient.discovery import build

class ApiCrawler():
    def __init__(self,video_id):
        self.api_key = 'AIzaSyB2TSRWOgMYsy8o5KZVo2wxwtro52QX9tM'
        self.video_id = video_id
    
    def get_comments(self):
        replies = []
  
        # creating youtube resource object
        youtube = build('youtube', 'v3',
                        developerKey=api_key)
  
        # retrieve youtube video results
        video_response=youtube.commentThreads().list(
        maxResults = 100,
        part='snippet,replies',
        videoId=video_id
        ).execute()
  
        # iterate video response
        while video_response:
        
            # extracting required info
            # from each result object 
            for item in video_response['items']:
            
                # Extracting comments
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
              
                # counting number of reply of comment
                replycount = item['snippet']['totalReplyCount']
  
                # if reply is there
                if replycount>0:
                
                    # iterate through all reply
                    for reply in item['replies']['comments']:
                    
                        # Extract reply
                        reply = reply['snippet']['textDisplay']
                      
                        # Store reply is list
                        replies.append(reply)
  
                # print comment with list of reply
                print(comment, replies, end = '\n\n')
  
                # empty reply list
                replies = []
  
            # Again repeat
            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                        part = 'snippet,replies',
                        videoId = video_id,
                        pageToken = video_response['nextPageToken']
                    ).execute()
            else:
                break

        def get_thumbnail(self):
            pass

        def get_sound(self):
            pass

        def get_live_chat(self):
            pass
