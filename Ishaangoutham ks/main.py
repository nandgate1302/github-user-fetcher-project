import json
import requests
username = input("enter the username : ").strip()
api = f"https://api.github.com/users/{username}"
repos_api = f"https://api.github.com/users/{username}/repos"
profile = requests.get(api)
repos = requests.get(repos_api)
if profile.status_code != 200:
    print("ERROR")
    print("error is",profile.status_code)
else:
    user_data=profile.json()
    print("name : ",user_data.get('name'))
    print("username : ",user_data.get('login'))
    print("bio: ",user_data.get('bio'))
    print("followers : ",user_data.get('followers'))
    print("following : ",user_data.get('following'))
    print("public repositories : ",user_data.get('public_repos'))
    print("account Creation Date : ",user_data.get('created_at'))
if repos.status_code == 200:
    repos_data=repos.json()
    c=0
    for i in repos_data[:5]:
        print("repos name",i.get('name'))
else:
    print("error")