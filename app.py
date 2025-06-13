from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
app = Flask(__name__)

def check_url_google(url):
    API_KEY = os.getenv("GOOGLE_API_KEY")
    payload = {
        "client": {
            "clientId": "phishshield",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        response = requests.post(
            f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}",
            json=payload,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("url", "").strip()
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    if not url.startswith(("http://", "https://")):
        return render_template("result.html", 
               risk="⚠️ Invalid", 
               reason="URL must start with http:// or https://",
               now=current_time,
               url=url)
    
    result = check_url_google(url)
    
    if "error" in result:
        return render_template("result.html", 
               risk="⚠️ API Error", 
               reason=result["error"],
               now=current_time,
               url=url)
    
    if "matches" in result:
        threat = result["matches"][0]["threatType"]
        return render_template("result.html", 
               risk="❌ MALICIOUS", 
               reason=f"Google detected: {threat.replace('_', ' ').title()}",
               now=current_time,
               url=url)
    
    return render_template("result.html", 
           risk="✅ Safe", 
           reason="No threats found",
           now=current_time,
           url=url)

if __name__ == "__main__":
    app.run(debug=True)