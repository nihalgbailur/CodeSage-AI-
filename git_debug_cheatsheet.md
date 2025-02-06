# **🚀 Git & GitHub Error Debugging Cheat Sheet** 🛠️

This cheat sheet covers **common Git errors** and their solutions, helping you troubleshoot and resolve issues quickly. 💡

---

## **1️⃣ Fixing Push Errors**

### **🔹 `! [rejected] main -> main (fetch first)`**
**Error Message:**
```bash
error: failed to push some refs to 'https://github.com/user/repo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally.
```
✅ **Fix: Sync local branch with remote before pushing**
```bash
git fetch origin  # Fetch latest changes
git pull origin main --rebase  # Rebase remote changes into your branch
git push origin main  # Push changes
```
⚠ **Force Push (DANGER ⚠️ - Overwrites Remote History)**
```bash
git push origin main --force
```
---

### **🔹 `fatal: remote origin already exists`**
**Error Message:**
```bash
fatal: remote origin already exists.
```
✅ **Fix: Remove and re-add the correct remote URL**
```bash
git remote remove origin
git remote add origin https://github.com/user/repo.git
git push -u origin main
```
---

## **2️⃣ Fixing Merge Conflicts**

### **🔹 `CONFLICT (content): Merge conflict in <file>`**
**Error Message:**
```bash
Automatic merge failed; fix conflicts and then commit the result.
```
✅ **Fix: Resolve conflicts manually**
1. Open the conflicting file.
2. Look for conflict markers:
   ```
   <<<<<<< HEAD
   Your local changes
   =======
   Remote changes
   >>>>>>> origin/main
   ```
3. Edit the file to keep the correct version.
4. Mark conflicts as resolved:
   ```bash
   git add <file>
   git commit -m "Resolved merge conflict"
   git push origin main
   ```
---

## **3️⃣ Authentication & Permission Issues**

### **🔹 `remote: Repository not found`**
**Error Message:**
```bash
remote: Repository not found.
fatal: repository 'https://github.com/user/repo.git/' not found
```
✅ **Fix: Check repository URL and access permissions**
```bash
git remote -v  # Check if the correct URL is set
git remote set-url origin https://github.com/user/repo.git
```

---

### **🔹 `fatal: Authentication failed`**
✅ **Fix: Use a GitHub Personal Access Token (PAT) instead of a password**
1. Go to **GitHub → Settings → Developer Settings → Personal Access Tokens**.
2. Generate a **new token** with **repo access**.
3. Use the token instead of a password:
   ```bash
   git remote set-url origin https://user:<your-personal-access-token>@github.com/user/repo.git
   ```

---

## **4️⃣ Undoing Mistakes**

### **🔹 Undo the Last Commit (Before Pushing)**
```bash
git reset --soft HEAD~1  # Undo commit, keep changes
git reset --hard HEAD~1  # Undo commit and discard changes
```

### **🔹 Revert a Pushed Commit**
```bash
git revert <commit-hash>
git push origin main
```

### **🔹 Discard All Local Changes**
```bash
git checkout .
git clean -fd
```

---

## **5️⃣ Cloning & Updating Repositories**

### **🔹 Clone a Repository**
```bash
git clone https://github.com/user/repo.git
```

### **🔹 Update Local Repo with Latest Changes**
```bash
git pull origin main
```

---

## **6️⃣ Essential Git Commands**

| **Command** | **Description** |
|------------|----------------|
| `git init` | Initialize a new Git repository |
| `git add .` | Stage all changes for commit |
| `git commit -m "message"` | Commit staged changes with a message |
| `git push origin main` | Push changes to GitHub |
| `git pull origin main` | Fetch and merge latest changes |
| `git status` | Check the status of your repository |
| `git log --oneline` | View commit history |
| `git branch -M main` | Rename the branch to main |
| `git remote -v` | View remote repository URLs |
| `git diff` | See unstaged changes |

---

### **🚀 Cheat Sheet Summary**
✅ **Fix Push Errors:** Sync your branch before pushing.  
✅ **Resolve Merge Conflicts:** Manually edit and commit.  
✅ **Fix Authentication Issues:** Use a GitHub token.  
✅ **Undo Mistakes:** Reset commits, revert changes.  
✅ **Keep Repo Updated:** Regularly pull the latest changes.  

🔥 **Master Git & GitHub Debugging!** 🚀

