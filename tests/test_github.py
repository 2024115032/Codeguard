import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(
    "https://api.github.com/user",
    headers=headers
)

print("GitHub API Status:", response.status_code)

if response.status_code == 200:
    print("GitHub token is working!")
else:
    print("GitHub token test failed.")