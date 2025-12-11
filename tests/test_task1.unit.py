import unittest
import sys
from io import StringIO


class TestTask1(unittest.TestCase):
    
    def setUp(self):
        """Capture output and import student code"""
        # Capture stdout
        self.held_output = StringIO()
        sys.stdout = self.held_output
        
        # Import student code (this will execute their print statements)
        try:
            import task1
            self.task1 = task1
        except Exception as e:
            self.fail(f"Failed to import task1.py: {e}")
        
        # Restore stdout and get output
        sys.stdout = sys.__stdout__
        self.output = self.held_output.getvalue()
    
    def test_all_requirements(self):
        """Verify all variables and output are correct"""
        
        # Check all variables exist and have correct values
        self.assertTrue(hasattr(self.task1, 'current_milestone'), 
                       "Variable 'current_milestone' not found")
        self.assertEqual(self.task1.current_milestone, 4, 
                        "current_milestone is miscalculated")
        
        self.assertTrue(hasattr(self.task1, 'progress_in_milestone'), 
                       "Variable 'progress_in_milestone' not found")
        self.assertEqual(self.task1.progress_in_milestone, 567, 
                        "progress_in_milestone is miscalculated")
        
        self.assertTrue(hasattr(self.task1, 'total_gained'), 
                       "Variable 'total_gained' not found")
        self.assertEqual(self.task1.total_gained, 2467, 
                        "total_gained is miscalculated")
        
        self.assertTrue(hasattr(self.task1, 'daily_average'), 
                       "Variable 'daily_average' not found")
        self.assertEqual(self.task1.daily_average, 54, 
                        "daily_average is miscalculated")
        
        self.assertTrue(hasattr(self.task1, 'days_to_milestone'), 
                       "Variable 'days_to_milestone' not found")
        self.assertEqual(self.task1.days_to_milestone, 8, 
                        "days_to_milestone is miscalculated")
        
        self.assertTrue(hasattr(self.task1, 'weekly_growth'), 
                       "Variable 'weekly_growth' not found")
        self.assertEqual(self.task1.weekly_growth, 378, 
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
        self.assertEqual(self.output, expected_output, 
                        "Output format does not match expected format")


if __name__ == '__main__':
    unittest.main()
