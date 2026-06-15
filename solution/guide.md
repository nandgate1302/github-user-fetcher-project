# GitHub User Fetcher 🚀

A beginner-friendly Python project that demonstrates how to consume APIs and work with JSON data.

The application takes a GitHub username as input, fetches the user's information using the GitHub API, and displays it in the terminal or a graphical interface.

---

## Features

### Minimum Requirements

- Fetch GitHub user information using the GitHub API.
- Display:
  - Name
  - Username
  - Bio
  - Followers
  - Following
  - Public Repositories
  - Account Creation Date
- Handle invalid usernames gracefully.

### Bonus Features

- Display the user's top 5 repositories.
- Save user data to a JSON file.
- GUI version built with Tkinter.

---

## Project Structure

```text
.
├── main.py
├── bonus.py
├── ui.py
├── requirements.txt
└── GUIDE.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mulearngectcr/github-user-fetcher-project.git
cd github-user-fetcher-project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Minimum Solution

```bash
python main.py
```

### Bonus Solution

```bash
python bonus.py
```

### GUI Version

```bash
python ui.py
```

---

## Example

Input:

```text
Enter GitHub username: torvalds
```

Output:

```text
===== GitHub User Details =====
Name                : Linus Torvalds
Username            : torvalds
Bio                 : Software Engineer
Followers           : ...
Following           : ...
Public Repositories : ...
Account Created On  : ...
```

---

## GitHub API Endpoint Used

```text
https://api.github.com/users/<username>
```

Example:

```text
https://api.github.com/users/torvalds
```

---

## Contributing

Want to submit your solution?

1. Fork this repository.
2. Create a folder with your name.
3. Add your solution files.
4. Commit and push your changes.
5. Open a Pull Request.

Detailed instructions can be found in the repository's contribution guide.

---

## Learning Outcomes

By completing this project, you will learn:

- What APIs are and how they work.
- Making HTTP requests in Python.
- Parsing JSON responses.
- Error handling.
- Building simple CLI and GUI applications.
- Working with external APIs.

---

Happy coding! 🚀
