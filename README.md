# 🔍 PhishDetect
A modern web application that detects phishing/malicious URLs using Google Safe Browsing API.


## ✨ Features

- 🕵️‍♂️ Real-time URL scanning against Google's threat database
- 📊 Detailed threat analysis with timestamps
- 🔐 Secure API key management (via `.env`)

## 🛠️ Tech Stack

| Component      | Technology |
|----------------|------------|
| Frontend       | HTML5, CSS3, JavaScript |
| Backend        | Python Flask |
| API            | Google Safe Browsing v4 |
| Security       | Environment variables |


### Installation

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file:
cp .env.example .env

#Add your Google API key:
GOOGLE_API_KEY=your_key_here

#Running Locally
python app.py
Visit http://localhost:5000 in your browser.
