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
        import task1
        sys.stdout = sys.__stdout__
        output = held_output.getvalue()
        return task1, output
    except Exception as e:
        sys.stdout = sys.__stdout__
        pytest.fail(f"Failed to import task1.py: {e}")


# ============= VARIABLE TESTS (4 points) =============

def test_current_milestone_variable(student_code):
    """Test current_milestone variable exists and equals 4 (1 point)"""
    task1, output = student_code
    assert hasattr(task1, 'current_milestone'), "Variable 'current_milestone' not found"
    assert task1.current_milestone == 4, f"Expected current_milestone to be 4, got {task1.current_milestone}"


def test_progress_in_milestone_variable(student_code):
    """Test progress_in_milestone variable exists and equals 567 (1 point)"""
    task1, output = student_code
    assert hasattr(task1, 'progress_in_milestone'), "Variable 'progress_in_milestone' not found"
    assert task1.progress_in_milestone == 567, f"Expected progress_in_milestone to be 567, got {task1.progress_in_milestone}"


def test_total_gained_variable(student_code):
    """Test total_gained variable exists and equals 2467 (1 point)"""
    task1, output = student_code
    assert hasattr(task1, 'total_gained'), "Variable 'total_gained' not found"
    assert task1.total_gained == 2467, f"Expected total_gained to be 2467, got {task1.total_gained}"


def test_daily_average_variable(student_code):
    """Test daily_average variable exists and equals 54 (1 point)"""
    task1, output = student_code
    assert hasattr(task1, 'daily_average'), "Variable 'daily_average' not found"
    assert task1.daily_average == 54, f"Expected daily_average to be 54, got {task1.daily_average}"


# ============= CALCULATION TESTS (3 points) =============

def test_days_to_milestone_calculation(student_code):
    """Test days_to_milestone calculation - check variable first, fallback to output (1 point)"""
    task1, output = student_code
    
    # Try to check variable first
    try:
        assert hasattr(task1, 'days_to_milestone'), "Variable 'days_to_milestone' not found"
        assert task1.days_to_milestone == 8, f"Expected days_to_milestone to be 8, got {task1.days_to_milestone}"
    except AssertionError:
        # Fallback: check if correct value appears in output
        assert "Days to Next Milestone: 8" in output, \
            "days_to_milestone variable is incorrect and value not found in output"


def test_weekly_growth_calculation(student_code):
    """Test weekly_growth calculation - check variable first, fallback to output (1 point)"""
    task1, output = student_code
    
    # Try to check variable first
    try:
        assert hasattr(task1, 'weekly_growth'), "Variable 'weekly_growth' not found"
        assert task1.weekly_growth == 378, f"Expected weekly_growth to be 378, got {task1.weekly_growth}"
    except AssertionError:
        # Fallback: check if correct value appears in output
        assert "Weekly Growth Projection: 378" in output, \
            "weekly_growth variable is incorrect and value not found in output"


def test_calculations_are_integers(student_code):
    """Test that calculations produce integer results (suggests // was used) (1 point)"""
    task1, output = student_code
    
    # Check that key calculations are integers, not floats
    if hasattr(task1, 'current_milestone'):
        assert isinstance(task1.current_milestone, int), "current_milestone should be an integer (use //)"
    
    if hasattr(task1, 'daily_average'):
        assert isinstance(task1.daily_average, int), "daily_average should be an integer (use //)"
    
    if hasattr(task1, 'days_to_milestone'):
        assert isinstance(task1.days_to_milestone, int), "days_to_milestone should be an integer (use //)"


# ============= OUTPUT STRUCTURE TESTS (3 points) =============

def test_output_has_all_lines(student_code):
    """Test output contains 7 lines (1 point)"""
    task1, output = student_code
    lines = output.strip().split('\n')
    assert len(lines) == 7, f"Expected 7 lines of output, got {len(lines)}"


def test_output_labels_correct(student_code):
    """Test output contains all required labels (1 point)"""
    task1, output = student_code
    
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
        assert label in output, f"Missing label: {label}"


def test_output_units_correct(student_code):
    """Test output contains correct units (followers/days) (1 point)"""
    task1, output = student_code
    
    # Check for "followers" appearing 5 times (Progress, Total Growth, Daily Average, Weekly Growth, and possibly other contexts)
    followers_count = output.count("followers")
    assert followers_count >= 4, f"Expected 'followers' to appear at least 4 times, found {followers_count}"
    
    # Check for "days" appearing at least once
    days_count = output.count("days")
    assert days_count >= 1, f"Expected 'days' to appear at least once, found {days_count}"
    
    # Verify specific lines have correct units
    assert re.search(r'Progress in Milestone: \d+ followers', output), \
        "Progress in Milestone line should end with 'followers'"
    assert re.search(r'Days to Next Milestone: \d+ days', output), \
        "Days to Next Milestone line should end with 'days'"
