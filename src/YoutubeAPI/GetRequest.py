from googleapiclient.discovery import build
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_video_details(video_id):
    """Fetch video details (title, views, likes) from YouTube API."""
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()

    if not response.get("items"):
        print("Invalid video ID or no data available.")
        return None

    video = response["items"][0]
    title = video["snippet"]["title"]
    views = video["statistics"].get("viewCount", "N/A")
    likes = video["statistics"].get("likeCount", "N/A")

    return {
        "Title": title,
        "Views": views,
        "Likes": likes
    }

# Example usage
video_id = "dQw4w9WgXcQ"  # Replace with any YouTube video ID
video_info = get_video_details(video_id)

if video_info:
    print(video_info)
