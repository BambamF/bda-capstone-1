# Phase 01: Preparation (15 minutes)

## Goal

Set up a clean Python development workspace for the capstone activity.

## What is a fork?

A fork is your own copy of someone else's GitHub repository. We use a fork so you can safely make changes, commit your work, and push to your own GitHub account without changing the instructor repository.

## Steps

1. Make sure Python is installed on your computer and your GitHub account is ready in your browser.

2. Open the [capstone repository](https://github.com/warestack/bda-capstone-1) in a new tab and return here.

3. Fork the repository to your own GitHub account.

Click `Fork` on the instructor repository.

![Fork the repository on GitHub](../assets/how-to-fork.png)

On the next screen, choose your GitHub account as the owner and click `Create fork`.

![Create a new fork on GitHub](../assets/create-fork.png)

4. After GitHub creates your fork, copy the HTTPS clone URL from your own repository. Make sure the URL contains your GitHub username.

Click the copy button.

![Clone your forked repository](../assets/clone-your-repo.png)

5. On your computer, open a new, **fresh VS Code** window and a terminal and navigate to a folder, for example `cd Documents`.

Then run:

```bash
git clone YOUR_HTTP_CLONE_URL
cd bda-capstone-1
```

6. Open the cloned folder in VS Code.

7. Create and activate a virtual environment.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> Optional temporary PowerShell bypass (current session only): `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` Then run: `.venv\Scripts\Activate.ps1`

8. Install the dependencies in the `requirements.txt`.

```bash
pip install -r requirements.txt
```

9. Create a simple test file called `solutions/test_yt_dlp.py` to check that `yt-dlp` installed correctly.

```python
import yt_dlp

print("Import successfully")
```

Run the test:

```bash
python solutions/test_yt_dlp.py
```

## Checkpoint

Before moving to Phase 02, confirm that:

- **You cloned your own fork, not the instructor repository.**

  Check your Git remote (you should see your own GitHub username in the remote URL).

  ```bash
  git remote -v
  ```

- The project folder is open in VS Code.
- You are in the correct folder (`bda-capstone-1`)
- Your virtual environment is activated.
- The dependencies were installed without errors.
- `python solutions/test_yt_dlp.py` prints `Import successfully`.
