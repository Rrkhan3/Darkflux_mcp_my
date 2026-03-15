from fastmcp import FastMCP
import os
import requests
from starlette.responses import PlainTextResponse

# १. Render को पोर्ट सेटअप
port = int(os.environ.get("PORT", 10000))
mcp = FastMCP("Darkflux-Ultimate-Server")

# २. यो भागले UptimeRobot लाई '200 OK' पठाउँछ (जसले गर्दा DOWN देखिदैन)
@mcp.app.get("/")
async def root():
    return PlainTextResponse("Darkflux Server is Running Successfully!")

# ३. तपाईँका टुलहरू (पहिल्यैका जस्तै)
@mcp.tool()
def video_ai_expert(topic: str):
    """होरर स्क्रिप्ट र एआई भिडियो रणनीति बनाउँछ।"""
    return {"script": f"{topic} को भयानक कथा...", "status": "Success"}

@mcp.tool()
def search_youtube_trends(query: str):
    """YouTube API प्रयोग गरेर ट्रेन्ड खोज्छ।"""
    YT_KEY = "AIzaSyAabApn_rOZMZsRHZ6LeOZqa0PlVKR0hmM"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YT_KEY}&maxResults=5"
    try:
        r = requests.get(url).json()
        videos = [item['snippet']['title'] for item in r.get('items', [])]
        return {"trending_videos": videos, "status": "Success"}
    except:
        return {"status": "Failed"}

# ४. सर्भर रन गर्ने तरिका
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=port)
