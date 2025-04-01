from googleapiclient.discovery import build
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)


def get_channel_id(search_item):
      try:
          """get channel ID"""
          request = youtube.search().list(
               part = "snippet",
               q= search_item,
               type = "video"
          )
          response = request.execute()
          return response["items"][0]["snippet"]["channelId"]
      except:
          print("there was an error")


def make_youtube_url(videoId, channelId):
     return f"https://youtube.com/watch?v={videoId}&ab_channel={channelId}"



def retrieve_video_id(search_item):
    try:
          """for retrieving the if x is streaming"""
          request = youtube.search().list(
               part = "snippet",
               q = search_item,
               eventType = "live",
               type="video",
               channelId = "UC9p_lqQ0FEDz327Vgf5JwqA"

          )
          response = request.execute()
          return response["items"][0]["id"]["videoId"]
    except:
          print("does not exist")

# Example usage
video_q = "Kaminari Clara"  # Replace with any YouTube video ID
video_info = retrieve_channel_id(video_q)

