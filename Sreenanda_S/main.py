import requests
user=input("Enter GitHub username:\n")
giturl=f"https://api.github.com/users/{user}"
output=requests.get(giturl)
if output.status_code==200:
    data=output.json()
    print("\n-------Github User Fetcher---------\n")
    print("\nGithub User Details\n")
    print(f"Name:{data.get('name')}")
    print(f"Username:{data.get('login')}")
    print(f"Bio:{data.get('bio')}")
    print(f"Followers:{data.get('followers')}")
    print(f"Following:{data.get('following')}")
    print(f"Public Repositories:{data.get('public_repos')}")
    print(f"Account Created On:{data.get('created_at')}")
else:
    print("User Not Found")