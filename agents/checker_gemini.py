# Final version of checker_gemini.py

import subprocess

def run_checker():
    print("🔍 Running checker on calculator.py")

    test_cases = [
        ("2", "+", "3", 5),
        ("10", "/", "0", "Error: Division by zero"),
        ("5", "-", "8", -3)
    ]

    results = []
    for a, op, b, expected in test_cases:
        try:
            # Run calculator.py and simulate inputs
            process = subprocess.Popen(
                ["python3", "calculator.py"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(f"{a}\n{op}\n{b}\n", timeout=5)
            output_lines = stdout.strip().split("\n")
            result_line = output_lines[-1] if output_lines else "No output"
            result = result_line.replace("Result:", "").strip()

            # Compare results
            match = str(expected) in result or result == str(expected)
            results.append((a, op, b, expected, result, match))
        except Exception as e:
            results.append((a, op, b, expected, str(e), False))

    # Write code review report
    with open("reviews/code_review_calculator.md", "w") as f:
        f.write("# Gemini Code Review for calculator.py\n\n")
        for a, op, b, expected, result, match in results:
            f.write(f"- Input: {a} {op} {b} → Expected: {expected}, Got: {result} → {'✅' if match else '❌'}\n")
        all_passed = all(match for _, _, _, _, _, match in results)
        f.write("\n**Result:** " + ("All tests passed ✅" if all_passed else "Some tests failed ❌"))

    print("✅ Checker completed. Results saved to reviews/code_review_calculator.md")

if __name__ == "__main__":
    run_checker()
