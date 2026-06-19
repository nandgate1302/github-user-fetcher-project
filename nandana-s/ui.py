import tkinter as tk
from tkinter import messagebox

from main import (
    fetch_user,
    fetch_top_repos,
    save_user_data
)


class GitHubUserFetcher:

    def __init__(self, root):

        self.root = root

        self.root.title("GitHub User Fetcher")
        self.root.geometry("750x650")

        title = tk.Label(
            root,
            text="GitHub User Fetcher",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        self.username_entry = tk.Entry(
            root,
            width=40,
            font=("Arial", 12)
        )
        self.username_entry.pack(pady=10)

        fetch_button = tk.Button(
            root,
            text="Fetch User",
            command=self.fetch_data
        )
        fetch_button.pack()

        self.result_text = tk.Text(
            root,
            width=90,
            height=30
        )
        self.result_text.pack(pady=15)

    def fetch_data(self):

        username = self.username_entry.get().strip()

        if not username:
            messagebox.showwarning(
                "Warning",
                "Please enter a username."
            )
            return

        user = fetch_user(username)

        if user is None:
            messagebox.showerror(
                "Error",
                "GitHub user not found."
            )
            return

        repos = fetch_top_repos(username)

        saved_file = save_user_data(user)

        self.result_text.delete(
            "1.0",
            tk.END
        )

        output = f"""
Name: {user.get('name')}
Username: {user.get('login')}
Bio: {user.get('bio')}

Followers: {user.get('followers')}
Following: {user.get('following')}

Public Repositories: {user.get('public_repos')}

Account Created:
{user.get('created_at')}

Saved To:
{saved_file}

------------------------
Top 5 Repositories
------------------------
"""

        for repo in repos:
            output += (
                f"\n{repo['name']} "
                f"(⭐ {repo['stargazers_count']})"
            )

        self.result_text.insert(
            tk.END,
            output
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = GitHubUserFetcher(root)

    root.mainloop()