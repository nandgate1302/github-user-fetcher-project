# This file contains solutions for the bonus challenges.
# Features:
# - Display top repositories
# - Save user data to a JSON file
# - Handle invalid usernames gracefully

import json
import requests

# Base endpoint for fetching GitHub users
BASE_URL = "https://api.github.com/users"


def get_user(username):
    """
    Fetches a GitHub user's details.

    Args:
        username (str): GitHub username.

    Returns:
        dict | None
    """
    response = requests.get(f"{BASE_URL}/{username}")

    if response.status_code != 200:
        return None

    return response.json()


def get_repositories(username):
    """
    Fetches repositories belonging to a GitHub user.

    Args:
        username (str): GitHub username.

    Returns:
        list: List of repositories.
    """
    response = requests.get(f"{BASE_URL}/{username}/repos")

    if response.status_code != 200:
        return []

    return response.json()


def save_to_json(username, data):
    """
    Saves user data to a JSON file.

    Args:
        username (str): GitHub username.
        data (dict): User data.
    """
    filename = f"{username}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\nUser data saved to '{filename}'")


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


def display_repositories(repositories):
    """
    Displays the top 5 repositories of the user.
    """
    print("\n===== Top Repositories =====")

    if not repositories:
        print("No repositories found.")
        return

    for index, repo in enumerate(repositories[:5], start=1):
        print(f"{index}. {repo['name']}")


def main():
    """
    Entry point of the bonus application.
    """
    # Get username input
    username = input("Enter GitHub username: ").strip()

    # Validate input
    if not username:
        print("Username cannot be empty.")
        return

    # Fetch user details
    user = get_user(username)

    # Handle invalid usernames
    if user is None:
        print("User not found.")
        return

    # Display user information
    display_user(user)

    # Fetch and display repositories
    repositories = get_repositories(username)
    display_repositories(repositories)

    # Save user data locally
    save_to_json(username, user)


if __name__ == "__main__":
    main()