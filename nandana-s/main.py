import os 
import requests
import json
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

base_url = "https://api.github.com/users"

HEADERS = {}
if TOKEN: 
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

def fetch_user(username): 
    url = f"{base_url}/{username}"

    try: 
        response = requests.get(url, headers = HEADERS, timeout = 10)
        
        #if the response is a 4xx or 5xx (HTTPerror), jumps to except block
        response.raise_for_status()

        return response.json()
    
    except requests.exceptions.RequestException:
        return None


def fetch_top_repos(username):

    url = f"{base_url}/{username}/repos"

    try:
        responses = requests.get(url, headers=HEADERS, timeout=10)

        responses.raise_for_status()

        repos = responses.json()

        repos.sort(key=lambda repo: repo["stargazers_count"], reverse=True)

        return repos[:5]
    
    except requests.exceptions.RequestException:
        return []
    
def save_user_data(user_data):
    os.makedirs("saved_users", exist_ok=True)
    filename = f"saved_users/{user_data["login"]}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4)
    
    return filename
