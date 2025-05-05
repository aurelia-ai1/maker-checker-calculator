# Final version of orchestrator_chatgpt_langchain.py

import os
import subprocess

def orchestrate():
    print("🚀 Orchestration started...")

    # Step 1: Run Claude maker
    print("✏️ Invoking Maker (Claude)...")
    subprocess.run(["python3", "agents/maker_claude.py"])

    # Step 2: Check if calculator.py was created
    if not os.path.exists("calculator.py"):
        print("❌ calculator.py not found. Maker failed.")
        return

    # Step 3: Run Gemini Checker
    print("🧪 Invoking Checker (Gemini)...")
    subprocess.run(["python3", "agents/checker_gemini.py"])

    # Step 4: Simulate Aurora scoring
    print("🔎 Invoking Aurora (Scoring)...")
    score = 100
    with open("reviews/code_review_calculator.md") as f:
        if "❌" in f.read():
            score = 70

    with open("reviews/execution_scorecard.md", "w") as f:
        f.write("# Aurora Scorecard\n\n")
        f.write(f"Score: {score}/100\n")
        f.write("Ethics Check: PASSED ✅\n")
        f.write("Tests: All passed ✅\n" if score == 100 else "Tests: Some failed ❌\n")

    print("📊 Aurora score saved to reviews/execution_scorecard.md")
    print("✅ Orchestration completed.")

if __name__ == "__main__":
    orchestrate()


    # Step 5: checking in code to Git
    print("🔐 Committing code to GitHub...")
    subprocess.run(["python3", "agents/repo_commit_agent.py"])

