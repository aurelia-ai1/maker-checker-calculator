import os
import subprocess

def commit_to_repo():
    repo_url = os.getenv("GITHUB_REPO_URL")
    github_token = os.getenv("GITHUB_PAT")

    if not repo_url or not github_token:
        print("❌ GitHub credentials not set in .env file.")
        return

    authed_repo = repo_url.replace("https://", f"https://{github_token}@")

    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "remote", "remove", "origin"], check=False)
        subprocess.run(["git", "remote", "add", "origin", authed_repo], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Update: new output from Maker-Checker POC"], check=True)

        # Switch or create branch safely
        try:
            subprocess.run(["git", "checkout", "-b", "feature/calculator-poc"], check=True)
        except subprocess.CalledProcessError:
            subprocess.run(["git", "checkout", "feature/calculator-poc"], check=True)

        subprocess.run(["git", "push", "-u", "origin", "feature/calculator-poc"], check=True)
        print("✅ Code pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("❌ Git push failed:", e)

if __name__ == "__main__":
    commit_to_repo()
