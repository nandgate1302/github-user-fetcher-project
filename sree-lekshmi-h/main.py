import tkinter as tk
import requests

def fetch_user():
    username = username_entry.get().strip()

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        created_at = data["created_at"]
        date = created_at.split("T")[0]

        details_text.delete("1.0", tk.END)

        details_text.insert(tk.END, "======= User Details =======\n\n")
        details_text.insert(tk.END, f"Name: {data['name']}\n")
        details_text.insert(tk.END, f"Username: {data['login']}\n")
        details_text.insert(tk.END, f"Bio: {data['bio']}\n")
        details_text.insert(tk.END, f"Followers: {data['followers']}\n")
        details_text.insert(tk.END, f"Following: {data['following']}\n")
        details_text.insert(tk.END, f"Public Repositories: {data['public_repos']}\n")
        details_text.insert(tk.END, f"Account Creation Date: {date}\n\n")

        url_repos = f"https://api.github.com/users/{username}/repos"
        response_repos = requests.get(url_repos)

        details_text.insert(tk.END, "Top 5 Repositories:\n")
        repos = response_repos.json()
        for repo in repos[:5]:
            details_text.insert(tk.END, f"• {repo['name']}\n")

    else:
        details_text.delete("1.0", tk.END)
        details_text.insert(tk.END, "User not found!")


root = tk.Tk()
root.title("GitHub User Fetcher")
root.geometry("600x500")

tk.Label(root, text="GitHub Username", font=("Arial", 12)).pack(pady=10)

username_entry = tk.Entry(root, width=30, font=("Arial", 12))
username_entry.pack()

tk.Button(
    root,
    text="Fetch Details",
    command=fetch_user,
    font=("Arial", 12)
).pack(pady=10)

details_text = tk.Text(root, width=70, height=20)
details_text.pack(pady=10)

root.mainloop()