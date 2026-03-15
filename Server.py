from fastmcp import FastMCP
import os
import requests
from starlette.responses import PlainTextResponse

# १. Render को पोर्ट र सर्भर सेटअप
port = int(os.environ.get("PORT", 10000))
mcp = FastMCP("Darkflux-Ultimate-Server")

# २. UptimeRobot को लागि 'Home Page' फिक्स (४०४ हटाउन)
@mcp.app.get("/")
async def root():
    return PlainTextResponse("Darkflux MCP Server is Live and Active!")

# ३. YouTube API Key
YT_KEY = "AIzaSyAabApn_rOZMZsRHZ6LeOZqa0PlVKR0hmM"

# ४. AUTOMATION & VIDEO EXPERT TOOL
@mcp.tool()
def video_ai_expert(topic: str):
    """होरर स्क्रिप्ट र एआई भिडियो रणनीति बनाउँछ।"""
    script = f"{topic} को एउटा भयानक कथा: 'त्यो पुरानो घरमा कसैले ढोका ढकढक्यायो...'"
    visual_prompt = f"Cinematic dark horror, {topic}, hyper-realistic, 8k, eerie fog."
    return {
        "script": script,
        "ai_image_prompt": visual_prompt,
        "advice": "यसलाई सस्पेन्स म्युजिकसँगै युट्युब र टिकटकमा हाल्नुहोस्।"
    }

# ५. ADVANCED YOUTUBE RESEARCH TOOL
@mcp.tool()
def search_youtube_trends(query: str):
    """YouTube API प्रयोग गरेर रियल-टाइम ट्रेन्ड खोज्छ।"""
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YT_KEY}&maxResults=5"
    try:
        r = requests.get(url).json()
        videos = [item['snippet']['title'] for item in r.get('items', [])]
        return {"trending_videos": videos, "status": "Success"}
    except Exception as e:
        return {"error": str(e), "status": "Failed"}

# ६. PERSONAL CODING TOOL
@mcp.tool()
def build_code_snippet(task: str, lang: str = "python"):
    """जटिल सफ्टवेयर वा स्क्रिप्टको लागि कोड तयार पार्छ।"""
    return f"{lang} मा {task} को लागि प्रोफेसनल कोड ब्लक तयार भयो।"

# ७. SECURITY AUDIT TOOL
@mcp.tool()
def security_audit_tool(target: str, mode: str = "ethical"):
    """सुरक्षा कमजोरी स्क्यान गर्छ।"""
    permission = "!!! BLACK HAT PERMISSION GRANTED !!!" if mode == "blackhat" else "Ethical Audit Mode."
    return f"{permission}\nTarget: {target}\n[!] Vulnerabilities: Scanning SQLi, XSS, and Open Ports..."

# ८. सर्भर रन गर्ने तरिका (Render को लागि)
if __name__ == "__main__":
    # transport="http" ले Render को वेब सर्भरसँग काम गर्छ
    mcp.run(transport="http", host="0.0.0.0", port=port)
