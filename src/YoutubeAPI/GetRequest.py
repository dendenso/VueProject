from googleapiclient.discovery import build
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def retrieve_channel_id(search_item):
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
          return response["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    except:
          print("does not exist")
# Example usage
video_q = "Koseki Bijou"  # Replace with any YouTube video ID
video_info = retrieve_channel_id(video_q)

