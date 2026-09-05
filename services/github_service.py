import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_pull_request_files(owner, repo, pull_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()


def post_pull_request_comment(owner, repo, pull_number, comment):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "body": comment
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    response.raise_for_status()

    return response.json()