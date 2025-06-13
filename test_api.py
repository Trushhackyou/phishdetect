import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

response = requests.get(
    "https://www.virustotal.com/api/v3/user/plan",
    headers={"x-apikey": API_KEY}
)
print(response.json())