# Final version of maker_claude.py

import os
import yaml

def generate_calculator_code():
    code = """
def calculate(a, b, operator):
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "Error: Division by zero"
            return a / b
        else:
            return "Error: Unknown operator"
    except Exception as e:
        return f"Exception occurred: {e}"

if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))
        result = calculate(a, b, operator)
        print("Result:", result)
    except Exception as e:
        print("Invalid input:", e)
"""
    with open("calculator.py", "w") as f:
        f.write(code.strip())
    print("✅ Calculator code generated to calculator.py")

if __name__ == "__main__":
    generate_calculator_code()
