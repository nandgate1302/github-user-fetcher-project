# This file contains the solution for the minimum requirements of the task.
# It fetches and displays basic GitHub user information using the GitHub API.

import requests

# Base endpoint for fetching GitHub users
BASE_URL = "https://api.github.com/users"


def get_user(username):
    """
    Fetches a GitHub user's details.

    Args:
        username (str): GitHub username.

    Returns:
        dict | None:
            Returns the user data as a dictionary if found,
            otherwise returns None.
    """
    url = f"{BASE_URL}/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def display_user(user):
    """
    Displays the required user information.
    """
    print("\n===== GitHub User Details =====")
    print(f"Name                : {user.get('name')}")
    print(f"Username            : {user.get('login')}")
    print(f"Bio                 : {user.get('bio')}")
    print(f"Followers           : {user.get('followers')}")
    print(f"Following           : {user.get('following')}")
    print(f"Public Repositories : {user.get('public_repos')}")
    print(f"Account Created On  : {user.get('created_at')}")


def main():
    """
    Entry point of the application.
    """
    # Take username input from the user
    username = input("Enter GitHub username: ").strip()

    # Validate empty input
    if not username:
        print("Username cannot be empty.")
        return

    # Fetch user details
    user = get_user(username)

    # Handle invalid usernames
    if user is None:
        print("User not found.")
        return

    # Display the fetched information
    display_user(user)


if __name__ == "__main__":
    main()