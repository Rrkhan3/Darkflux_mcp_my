from fastmcp import FastMCP
import os
import requests

# १. Render को पोर्ट सेटअप
port = int(os.environ.get("PORT", 10000))
mcp = FastMCP("Darkflux-Ultimate-Server")

# २. YouTube API Key
YT_KEY = "AIzaSyAabApn_rOZMZsRHZ6LeOZqa0PlVKR0hmM"

# ३. TOOLS SECTION
@mcp.tool()
def video_ai_expert(topic: str):
    """होरर स्क्रिप्ट र एआई भिडियो रणनीति बनाउँछ।"""
    script = f"{topic} को कथा: 'त्यो पुरानो घरमा को थियो?'"
    return {"script": script, "status": "Success"}

@mcp.tool()
def search_youtube_trends(query: str):
    """YouTube ट्रेन्ड खोज्छ।"""
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YT_KEY}&maxResults=5"
    try:
        r = requests.get(url).json()
        videos = [item['snippet']['title'] for item in r.get('items', [])]
        return {"trending_videos": videos, "status": "Success"}
    except Exception as e:
        return {"error": str(e), "status": "Failed"}

# ४. SERVER RUN (Render को लागि फिक्स गरिएको)
if __name__ == "__main__":
    # transport="http" ले गर्दा Render मा सर्भर अनलाइन रहन्छ
    mcp.run(transport="http", host="0.0.0.0", port=port)
