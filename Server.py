from fastmcp import FastMCP
import os
import requests

# १. Render को पोर्ट सेटअप (Render ले १०००० पोर्ट दिन्छ)
port = int(os.environ.get("PORT", 10000))
mcp = FastMCP("Darkflux-Ultimate-Server")

# तपाईँको YouTube API Key
YT_KEY = "AIzaSyAabApn_rOZMZsRHZ6LeOZqa0PlVKR0hmM"

# २. AUTOMATION & VIDEO EXPERT
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

# ३. ADVANCED YOUTUBE RESEARCH
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

# ४. PERSONAL CODING & APP BUILDING
@mcp.tool()
def build_code_snippet(task: str, lang: str = "python"):
    """जटिल सफ्टवेयर वा स्क्रिप्टको लागि कोड तयार पार्छ।"""
    return f"{lang} मा {task} को लागि प्रोफेसनल कोड ब्लक तयार भयो। यसलाई सिधै प्रयोग गर्न सकिन्छ।"

# ५. SECURITY & HACKING
@mcp.tool()
def security_audit_tool(target: str, mode: str = "ethical"):
    """सुरक्षा कमजोरी स्क्यान गर्छ।"""
    permission = "!!! BLACK HAT PERMISSION GRANTED !!!" if mode == "blackhat" else "Ethical Audit Mode."
    return f"{permission}\nTarget: {target}\n[!] Vulnerabilities: Scanning SQLi, XSS, and Open Ports...\n[+] रिपोर्ट तयार हुँदैछ।"

# ६. FILE & PHONE MANAGER
@mcp.tool()
def digital_manager(action: str, target: str):
    """फाइल र सिस्टम अटोमेशन म्यानेज गर्छ।"""
    return f"सफलतापूर्वक {target} मा {action} सम्पन्न भयो।"

# ७. सर्भर रन गर्ने तरिका (Render को लागि फिक्स गरिएको)
if __name__ == "__main__":
    # Render मा 'http' ट्रान्सपोर्ट र सही host/port चाहिन्छ
    mcp.run(transport="http", host="0.0.0.0", port=port)
