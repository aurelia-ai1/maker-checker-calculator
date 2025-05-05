# Final version of run_and_score.sh

#!/bin/bash

echo "🌐 Activating virtual environment..."
source venv/bin/activate

echo "🚀 Running full Calculator POC pipeline..."
python3 agents/orchestrator_chatgpt_langchain.py

echo ""
echo "📂 Output:"
cat reviews/code_review_calculator.md
echo ""
cat reviews/execution_scorecard.md
