# This file contains a simple GUI implementation of the
# GitHub User Fetcher using Tkinter.

import requests
import tkinter as tk
from tkinter import messagebox

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


def fetch_user():
    """
    Fetches user information and displays it in the GUI.
    """
    username = username_entry.get().strip()

    if not username:
        messagebox.showerror("Error", "Username cannot be empty.")
        return

    user = get_user(username)

    if user is None:
        messagebox.showerror("Error", "User not found.")
        return

    output_text.delete("1.0", tk.END)

    details = f"""
Name                : {user.get('name')}
Username            : {user.get('login')}
Bio                 : {user.get('bio')}
Followers           : {user.get('followers')}
Following           : {user.get('following')}
Public Repositories : {user.get('public_repos')}
Account Created On  : {user.get('created_at')}
"""

    output_text.insert(tk.END, details)


# Create the main window
root = tk.Tk()
root.title("GitHub User Fetcher")
root.geometry("600x350")

# Username label
label = tk.Label(root, text="Enter GitHub Username:")
label.pack(pady=(20, 5))

# Username input
username_entry = tk.Entry(root, width=40)
username_entry.pack()

# Search button
search_button = tk.Button(
    root,
    text="Fetch User",
    command=fetch_user
)
search_button.pack(pady=15)

# Output box
output_text = tk.Text(root, height=12, width=70)
output_text.pack(padx=20, pady=10)

# Start the GUI
root.mainloop()