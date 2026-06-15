import requests
from datetime import datetime

#fetching user

username=input("Enter your username: ")
api=f"https://api.github.com/users/{username}"    
result=requests.get(api)

if result.status_code==404:
    print(f"Error: {username} does not exist on GitHub.")
elif result.status_code==404:
    print(f"Error: Something went wrong. Error Status Code: {result.status_code}")
else:
    user_data=result.json() 
    name=user_data.get("name")
    login=user_data.get("login") 
    bio=user_data.get("bio")
    followers=user_data.get("followers")
    following=user_data.get("following")
    repos=user_data.get("public_repos")
    created_at=user_data.get("created_at")

    print("*"*50)
    print(f"Name: {name}")
    print(f"Username: {login}")
    print(f"Bio: {bio}")
    print(f"Followers: {followers} | Following: {following}")
    print(f"Public Repositories: {repos}")
    print(f"Account Created: {created_at}")
    print("*"*50)

#top 5 repos    
    repo=result.json()
    print("\n-----Top 5 Repositories-----")
    for i in range(5):
        print(f"{repo['name']}")
    print("----------------------------")

