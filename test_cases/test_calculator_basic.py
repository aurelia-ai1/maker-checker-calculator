# Final version of test_calculator_basic.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculator

def test_addition():
    assert calculator.calculate(2, 3, '+') == 5

def test_subtraction():
    assert calculator.calculate(10, 4, '-') == 6

def test_division_by_zero():
    assert calculator.calculate(10, 0, '/') == "Error: Division by zero"

def test_unknown_operator():
    assert "Error" in calculator.calculate(5, 2, '%')

