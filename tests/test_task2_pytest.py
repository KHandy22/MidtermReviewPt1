import pytest
import sys
from io import StringIO
import importlib

# Import task2 directly (for variable tests)
import task2


# ============= VARIABLE TESTS (4 points) =============

def test_balance_variable():
    """Test balance variable exists and equals 244 (1 point)"""
    assert hasattr(task2, 'balance'), "Variable 'balance' not found"
    assert task2.balance == 244, f"Expected balance to be 244, got {task2.balance}"


def test_total_monthly_fees_variable():
    """Test total_monthly_fees variable exists and equals 120 (1 point)"""
    assert hasattr(task2, 'total_monthly_fees'), "Variable 'total_monthly_fees' not found"
    assert task2.total_monthly_fees == 120, f"Expected total_monthly_fees to be 120, got {task2.total_monthly_fees}"


def test_full_twenties_variable():
    """Test full_twenties variable exists and equals 12 (1 point)"""
    assert hasattr(task2, 'full_twenties'), "Variable 'full_twenties' not found"
    assert task2.full_twenties == 12, f"Expected full_twenties to be 12, got {task2.full_twenties}"


def test_remaining_dollars_variable():
    """Test remaining_dollars variable exists and equals 4 (1 point)"""
    assert hasattr(task2, 'remaining_dollars'), "Variable 'remaining_dollars' not found"
    assert task2.remaining_dollars == 4, f"Expected remaining_dollars to be 4, got {task2.remaining_dollars}"


# ============= CALCULATION TESTS (3 points) =============

def test_balance_calculation(capsys):
    """Test balance calculation - check variable first, fallback to output (1 point)"""
    # Check variable first
    try:
        assert hasattr(task2, 'balance'), "Variable 'balance' not found"
        assert task2.balance == 244, f"Expected balance to be 244, got {task2.balance}"
    except AssertionError:
        # Fallback: check output
        captured = capsys.readouterr()
        assert "Remaining Balance: $244" in captured.out, \
            "balance variable is incorrect and value not found in output"


def test_twenties_calculation(capsys):
    """Test full_twenties and remaining_dollars calculations - check variables first, fallback to output (1 point)"""
    # Check variables first
    try:
        assert hasattr(task2, 'full_twenties'), "Variable 'full_twenties' not found"
        assert task2.full_twenties == 12, f"Expected full_twenties to be 12, got {task2.full_twenties}"
        assert hasattr(task2, 'remaining_dollars'), "Variable 'remaining_dollars' not found"
        assert task2.remaining_dollars == 4, f"Expected remaining_dollars to be 4, got {task2.remaining_dollars}"
    except AssertionError:
        # Fallback: check output
        captured = capsys.readouterr()
        assert "Full $20 Bills: 12" in captured.out and "Remaining Dollars: $4" in captured.out, \
            "twenties/dollars variables are incorrect and values not found in output"


def test_calculations_are_integers():
    """Test that calculations produce integer results (suggests // was used) (1 point)"""
    if hasattr(task2, 'balance'):
        assert isinstance(task2.balance, int), "balance should be an integer"
    
    if hasattr(task2, 'total_monthly_fees'):
        assert isinstance(task2.total_monthly_fees, int), "total_monthly_fees should be an integer"
    
    if hasattr(task2, 'full_twenties'):
        assert isinstance(task2.full_twenties, int), "full_twenties should be an integer (use //)"
    
    if hasattr(task2, 'remaining_dollars'):
        assert isinstance(task2.remaining_dollars, int), "remaining_dollars should be an integer (use %)"


# ============= OUTPUT STRUCTURE TESTS (3 points) =============

def test_output_has_all_lines(capsys):
    """Test output contains 4 lines (1 point)"""
    # Reimport to capture output
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert len(lines) == 4, f"Expected 4 lines of output, got {len(lines)}"


def test_output_labels_correct(capsys):
    """Test output contains all required labels (1 point)"""
    # Reimport to capture output
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    
    captured = capsys.readouterr()
    
    required_labels = [
        "Account Holder:",
        "Remaining Balance:",
        "Full $20 Bills:",
        "Remaining Dollars:"
    ]
    
    for label in required_labels:
        assert label in captured.out, f"Missing label: {label}"


def test_output_values_correct(capsys):
    """Test output contains correct values with proper formatting (1 point)"""
    # Reimport to capture output
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    
    captured = capsys.readouterr()
    output = captured.out
    
    # Check for specific formatted values
    assert "Taylor Banks" in output, "Account holder name not found in output"
    assert "$244" in output, "Balance value '$244' not found in output"
    assert "12" in output, "Full twenties value '12' not found in output"
    assert "$4" in output, "Remaining dollars value '$4' not found in output"


if __name__ == "__main__":
    pytest.main()
