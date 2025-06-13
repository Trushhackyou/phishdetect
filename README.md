# 🔍 PhishShield - AI-Powered Phishing Detection


A modern web application that detects phishing/malicious URLs using Google Safe Browsing API with dark/light mode toggle.


## ✨ Features

- 🕵️‍♂️ Real-time URL scanning against Google's threat database
- 🌗 Automatic dark/light mode with system preference detection
- 📊 Detailed threat analysis with timestamps
- 📱 Fully responsive design (works on mobile/desktop)
- 🔐 Secure API key management (via `.env`)

## 🛠️ Tech Stack

| Component       | Technology |
|----------------|------------|
| Frontend       | HTML5, CSS3, JavaScript |
| Backend        | Python Flask |
| API            | Google Safe Browsing v4 |
| Security       | Environment variables |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google API key ([Get one free](https://console.cloud.google.com/))

### Installation

# Clone repository
git clone https://github.com/your-username/phishshield.git
cd phishshield

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
