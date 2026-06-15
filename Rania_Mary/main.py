import requests

user = input("Enter GitHub username:\n")

url = f"https://api.github.com/users/{user}"

output = requests.get(url)

if output.status_code == 200:
    data = output.json()

    print("\n-------- GitHub User Fetcher --------\n")

    print(f"Name: {data.get('name')}")
    print(f"Username: {data.get('login')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Followers: {data.get('followers')}")
    print(f"Following: {data.get('following')}")
    print(f"Public Repositories: {data.get('public_repos')}")

    time = data.get("created_at", "").split("T")[0]
    print(f"Account Created On: {time}")

else:
    print("User Not Found")