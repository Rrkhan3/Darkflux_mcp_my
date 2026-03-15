from fastmcp import FastMCP
import os
import requests

# १. Render को पोर्ट सेटअप
port = int(os.environ.get("PORT", 10000))
mcp = FastMCP("Darkflux-Ultimate-Server")

# २. YouTube API Key
YT_KEY = "AIzaSyAabApn_rOZMZsRHZ6LeOZqa0PlVKR0hmM"

# ३. Health Check Resource (यसले UptimeRobot लाई डाउन हुन दिँदैन)
@mcp.resource("health://check")
def health_check() -> str:
    """सर्भर अनलाइन छ कि छैन चेक गर्छ।"""
    return "Darkflux Server is Running!"

# ४. तपाईँका टुलहरू
@mcp.tool()
def video_ai_expert(topic: str):
    """होरर स्क्रिप्ट र एआई भिडियो रणनीति बनाउँछ।"""
    return {"script": f"{topic} को कथा...", "status": "Success"}

@mcp.tool()
def search_youtube_trends(query: str):
    """YouTube API प्रयोग गरेर ट्रेन्ड खोज्छ।"""
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YT_KEY}&maxResults=5"
    try:
        r = requests.get(url).json()
        videos = [item['snippet']['title'] for item in r.get('items', [])]
        return {"trending_videos": videos, "status": "Success"}
    except:
        return {"status": "Failed"}

# ५. सर्भर रन गर्ने तरिका (FastMCP को आफ्नै सर्भर प्रयोग गर्ने)
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=port)
