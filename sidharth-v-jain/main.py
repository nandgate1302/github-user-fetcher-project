import requests
import json

user = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{user}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    print("\nGitHub User Details")
    print("-------------------------")
    print("Name:", data.get("name"))
    print("Username:", data.get("login"))
    print("Bio:", data.get("bio"))
    print("Followers:", data.get("followers"))
    print("Following:", data.get("following"))
    print("Public Repositories:", data.get("public_repos"))
    print("Account Creation Date:", data.get("created_at"))


    # JSON file
    user_data = {
        "Name": data.get("name"),
        "Username": data.get("login"),
        "Bio": data.get("bio"),
        "Followers": data.get("followers"),
        "Following": data.get("following"),
        "Public Repositories": data.get("public_repos"),
        "Account Creation Date": data.get("created_at")
    }

    fp = f"{user}_details.json"

    with open(fp, "w") as file:
        json.dump(user_data, file, indent=4)

    print(f"\nData saved to '{fp}'.")

elif response.status_code == 404:
    print("User not found.")
else:
    print("Error")
