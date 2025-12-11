import unittest
import sys
import os
from io import StringIO

# Ensure we can import from the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


class TestTask1(unittest.TestCase):
    
    def test_follower_tracker(self):
        """Verify all variables and output are correct"""
        
        # Capture stdout before importing
        held_output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = held_output
        
        # Import and reload to capture fresh output
        try:
            if 'task1' in sys.modules:
                del sys.modules['task1']
            import task1
        except Exception as e:
            sys.stdout = old_stdout
            self.fail(f"Failed to import task1.py: {e}")
        
        # Restore stdout and get output
        sys.stdout = old_stdout
        output = held_output.getvalue()
        
        # Check all variables exist and have correct values
        self.assertTrue(hasattr(task1, 'current_milestone'), 
                       "Variable 'current_milestone' not found")
        self.assertEqual(task1.current_milestone, 4, 
                        "current_milestone is miscalculated")
        
        self.assertTrue(hasattr(task1, 'progress_in_milestone'), 
                       "Variable 'progress_in_milestone' not found")
        self.assertEqual(task1.progress_in_milestone, 567, 
                        "progress_in_milestone is miscalculated")
        
        self.assertTrue(hasattr(task1, 'total_gained'), 
                       "Variable 'total_gained' not found")
        self.assertEqual(task1.total_gained, 2467, 
                        "total_gained is miscalculated")
        
        self.assertTrue(hasattr(task1, 'daily_average'), 
                       "Variable 'daily_average' not found")
        self.assertEqual(task1.daily_average, 54, 
                        "daily_average is miscalculated")
        
        self.assertTrue(hasattr(task1, 'days_to_milestone'), 
                       "Variable 'days_to_milestone' not found")
        self.assertEqual(task1.days_to_milestone, 8, 
                        "days_to_milestone is miscalculated")
        
        self.assertTrue(hasattr(task1, 'weekly_growth'), 
                       "Variable 'weekly_growth' not found")
        self.assertEqual(task1.weekly_growth, 378, 
                        "weekly_growth is miscalculated")
        
        # Check output format
        expected_output = """Creator: DigitalDreamer
Current Milestone: 4
Progress in Milestone: 567 followers
Total Growth: 2467 followers
Daily Average: 54 followers
Days to Next Milestone: 8 days
Weekly Growth Projection: 378 followers
"""
        self.assertEqual(output, expected_output, 
                        "Output format does not match expected format")


if __name__ == '__main__':
    unittest.main()
