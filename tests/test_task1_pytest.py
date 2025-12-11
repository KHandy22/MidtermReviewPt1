import pytest
import sys
from io import StringIO
import importlib

# Import task1 directly (for variable tests)
import task1


# ============= VARIABLE TESTS (4 points) =============

def test_current_milestone_variable():
    """Test current_milestone variable exists and equals 4 (1 point)"""
    assert hasattr(task1, 'current_milestone'), "Variable 'current_milestone' not found"
    assert task1.current_milestone == 4, f"Expected current_milestone to be 4, got {task1.current_milestone}"


def test_progress_in_milestone_variable():
    """Test progress_in_milestone variable exists and equals 567 (1 point)"""
    assert hasattr(task1, 'progress_in_milestone'), "Variable 'progress_in_milestone' not found"
    assert task1.progress_in_milestone == 567, f"Expected progress_in_milestone to be 567, got {task1.progress_in_milestone}"


def test_total_gained_variable():
    """Test total_gained variable exists and equals 2467 (1 point)"""
    assert hasattr(task1, 'total_gained'), "Variable 'total_gained' not found"
    assert task1.total_gained == 2467, f"Expected total_gained to be 2467, got {task1.total_gained}"


def test_daily_average_variable():
    """Test daily_average variable exists and equals 54 (1 point)"""
    assert hasattr(task1, 'daily_average'), "Variable 'daily_average' not found"
    assert task1.daily_average == 54, f"Expected daily_average to be 54, got {task1.daily_average}"


# ============= CALCULATION TESTS (3 points) =============

def test_days_to_milestone_calculation(capsys):
    """Test days_to_milestone calculation - check variable first, fallback to output (1 point)"""
    # Check variable first
    try:
        assert hasattr(task1, 'days_to_milestone'), "Variable 'days_to_milestone' not found"
        assert task1.days_to_milestone == 8, f"Expected days_to_milestone to be 8, got {task1.days_to_milestone}"
    except AssertionError:
        # Fallback: check output
        captured = capsys.readouterr()
        assert "Days to Next Milestone: 8" in captured.out, \
            "days_to_milestone variable is incorrect and value not found in output"


def test_weekly_growth_calculation(capsys):
    """Test weekly_growth calculation - check variable first, fallback to output (1 point)"""
    # Check variable first
    try:
        assert hasattr(task1, 'weekly_growth'), "Variable 'weekly_growth' not found"
        assert task1.weekly_growth == 378, f"Expected weekly_growth to be 378, got {task1.weekly_growth}"
    except AssertionError:
        # Fallback: check output
        captured = capsys.readouterr()
        assert "Weekly Growth Projection: 378" in captured.out, \
            "weekly_growth variable is incorrect and value not found in output"


def test_calculations_are_integers():
    """Test that calculations produce integer results (suggests // was used) (1 point)"""
    if hasattr(task1, 'current_milestone'):
        assert isinstance(task1.current_milestone, int), "current_milestone should be an integer (use //)"
    
    if hasattr(task1, 'daily_average'):
        assert isinstance(task1.daily_average, int), "daily_average should be an integer (use //)"
    
    if hasattr(task1, 'days_to_milestone'):
        assert isinstance(task1.days_to_milestone, int), "days_to_milestone should be an integer (use //)"


# ============= OUTPUT STRUCTURE TESTS (3 points) =============

def test_output_has_all_lines(capsys):
    """Test output contains 7 lines (1 point)"""
    # Reimport to capture output
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    assert len(lines) == 7, f"Expected 7 lines of output, got {len(lines)}"


def test_output_labels_correct(capsys):
    """Test output contains all required labels (1 point)"""
    # Reimport to capture output
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    
    captured = capsys.readouterr()
    
    required_labels = [
        "Creator:",
        "Current Milestone:",
        "Progress in Milestone:",
        "Total Growth:",
        "Daily Average:",
        "Days to Next Milestone:",
        "Weekly Growth Projection:"
    ]
    
    for label in required_labels:
        assert label in captured.out, f"Missing label: {label}"


def test_output_units_correct(capsys):
    """Test output contains correct units (followers/days) (1 point)"""
    # Reimport to capture output
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    
    captured = capsys.readouterr()
    output = captured.out
    
    # Check for "followers" appearing multiple times
    followers_count = output.count("followers")
    assert followers_count >= 4, f"Expected 'followers' to appear at least 4 times, found {followers_count}"
    
    # Check for "days" appearing at least once
    days_count = output.count("days")
    assert days_count >= 1, f"Expected 'days' to appear at least once, found {days_count}"


if __name__ == "__main__":
    pytest.main()
