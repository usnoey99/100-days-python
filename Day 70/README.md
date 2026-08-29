# Day 70 - Git, github, and Version Control

---

## 📌 Overview
Learn the basics of Git, Github, and version control for managing and tracking project changes.

Practice Site: https://learngitbranching.js.org/

---

## 🧠 Note

### Version Control
- A system for tracking changes to files over time.
- Allows to view, compare, and restore previous versions.

### Git Areas
```text
Working Directory
       ↓ git add
Staging Area
       ↓ git commit
Repository
```
- Working Directory: Files you are currently working on.
- Staging Area: A place to prepare changes for the next commit.
- Repository: Stores commited versions of the project.

### Basic Commends
```commandline
git init                    # Initialize a Git repository
git status                  # Check the current status
git add <file>              # Stage a file
git add .                   # Stage all changes
git commit -m "message"     # Create a commit
git log --oneline           # View commit history
git diff                    # View unstaged changes
git diff --staged           # View staged changes
```

### Forking and Requests
**Forking** is the process of creating a personal copy of someone else's repository on GitHub. It allows us to make changes to a project without directly modifying the original repository.  

After forking a repository, we can **clone** it to our computer, make changes, and **push** those changes to our fork.  

A *Pull Request*** is a request to merge your chages into the original repository. Other developers can review your code, leave comments, and suggest changes before the pull request is merged.