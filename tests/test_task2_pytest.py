import pytest
import sys
from io import StringIO
import re


@pytest.fixture(scope="module")
def student_code():
    """Import student code and capture output"""
    # Capture stdout
    held_output = StringIO()
    sys.stdout = held_output
    
    # Import student code
    try:
        import task2
        sys.stdout = sys.__stdout__
        output = held_output.getvalue()
        return task2, output
    except Exception as e:
        sys.stdout = sys.__stdout__
        pytest.fail(f"Failed to import task2.py: {e}")


# ============= VARIABLE TESTS (4 points) =============

def test_balance_variable(student_code):
    """Test balance variable exists and equals 244 (1 point)"""
    task2, output = student_code
    assert hasattr(task2, 'balance'), "Variable 'balance' not found"
    assert task2.balance == 244, f"Expected balance to be 244, got {task2.balance}"


def test_total_monthly_fees_variable(student_code):
    """Test total_monthly_fees variable exists and equals 120 (1 point)"""
    task2, output = student_code
    assert hasattr(task2, 'total_monthly_fees'), "Variable 'total_monthly_fees' not found"
    assert task2.total_monthly_fees == 120, f"Expected total_monthly_fees to be 120, got {task2.total_monthly_fees}"


def test_full_twenties_variable(student_code):
    """Test full_twenties variable exists and equals 12 (1 point)"""
    task2, output = student_code
    assert hasattr(task2, 'full_twenties'), "Variable 'full_twenties' not found"
    assert task2.full_twenties == 12, f"Expected full_twenties to be 12, got {task2.full_twenties}"


def test_remaining_dollars_variable(student_code):
    """Test remaining_dollars variable exists and equals 4 (1 point)"""
    task2, output = student_code
    assert hasattr(task2, 'remaining_dollars'), "Variable 'remaining_dollars' not found"
    assert task2.remaining_dollars == 4, f"Expected remaining_dollars to be 4, got {task2.remaining_dollars}"


# ============= CALCULATION TESTS (3 points) =============

def test_balance_calculation(student_code):
    """Test balance calculation - check variable first, fallback to output (1 point)"""
    task2, output = student_code
    
    # Try to check variable first
    try:
        assert hasattr(task2, 'balance'), "Variable 'balance' not found"
        assert task2.balance == 244, f"Expected balance to be 244, got {task2.balance}"
    except AssertionError:
        # Fallback: check if correct value appears in output
        assert "Remaining Balance: $244" in output, \
            "balance variable is incorrect and value not found in output"


def test_twenties_calculation(student_code):
    """Test full_twenties and remaining_dollars calculations - check variables first, fallback to output (1 point)"""
    task2, output = student_code
    
    # Try to check variables first
    try:
        assert hasattr(task2, 'full_twenties'), "Variable 'full_twenties' not found"
        assert task2.full_twenties == 12, f"Expected full_twenties to be 12, got {task2.full_twenties}"
        assert hasattr(task2, 'remaining_dollars'), "Variable 'remaining_dollars' not found"
        assert task2.remaining_dollars == 4, f"Expected remaining_dollars to be 4, got {task2.remaining_dollars}"
    except AssertionError:
        # Fallback: check if correct values appear in output
        assert "Full $20 Bills: 12" in output and "Remaining Dollars: $4" in output, \
            "twenties/dollars variables are incorrect and values not found in output"


def test_calculations_are_integers(student_code):
    """Test that calculations produce integer results (suggests // was used) (1 point)"""
    task2, output = student_code
    
    # Check that key calculations are integers, not floats
    if hasattr(task2, 'balance'):
        assert isinstance(task2.balance, int), "balance should be an integer"
    
    if hasattr(task2, 'total_monthly_fees'):
        assert isinstance(task2.total_monthly_fees, int), "total_monthly_fees should be an integer"
    
    if hasattr(task2, 'full_twenties'):
        assert isinstance(task2.full_twenties, int), "full_twenties should be an integer (use //)"
    
    if hasattr(task2, 'remaining_dollars'):
        assert isinstance(task2.remaining_dollars, int), "remaining_dollars should be an integer (use %)"


# ============= OUTPUT STRUCTURE TESTS (3 points) =============

def test_output_has_all_lines(student_code):
    """Test output contains 4 lines (1 point)"""
    task2, output = student_code
    lines = output.strip().split('\n')
    assert len(lines) == 4, f"Expected 4 lines of output, got {len(lines)}"


def test_output_labels_correct(student_code):
    """Test output contains all required labels (1 point)"""
    task2, output = student_code
    
    required_labels = [
        "Account Holder:",
        "Remaining Balance:",
        "Full $20 Bills:",
        "Remaining Dollars:"
    ]
    
    for label in required_labels:
        assert label in output, f"Missing label: {label}"


def test_output_values_correct(student_code):
    """Test output contains correct values with proper formatting (1 point)"""
    task2, output = student_code
    
    # Check for specific formatted values
    assert "Taylor Banks" in output, "Account holder name not found in output"
    assert "$244" in output, "Balance value '$244' not found in output"
    assert "12" in output, "Full twenties value '12' not found in output"
    assert "$4" in output, "Remaining dollars value '$4' not found in output"
