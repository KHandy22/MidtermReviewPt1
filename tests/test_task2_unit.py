import unittest
import sys
import os
from io import StringIO

# Ensure we can import from the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


class TestTask2(unittest.TestCase):
    
    def test_abandoned_bank_account(self):
        """Verify all variables and output are correct"""
        
        # Capture stdout before importing
        held_output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = held_output
        
        # Import and reload to capture fresh output
        try:
            if 'task2' in sys.modules:
                del sys.modules['task2']
            import task2
        except Exception as e:
            sys.stdout = old_stdout
            self.fail(f"Failed to import task2.py: {e}")
        
        # Restore stdout and get output
        sys.stdout = old_stdout
        output = held_output.getvalue()
        
        # Check all variables exist and have correct values
        self.assertTrue(hasattr(task2, 'balance'), 
                       "Variable 'balance' not found")
        self.assertEqual(task2.balance, 244, 
                        "balance is miscalculated")
        
        self.assertTrue(hasattr(task2, 'total_monthly_fees'), 
                       "Variable 'total_monthly_fees' not found")
        self.assertEqual(task2.total_monthly_fees, 120, 
                        "total_monthly_fees is miscalculated")
        
        self.assertTrue(hasattr(task2, 'full_twenties'), 
                       "Variable 'full_twenties' not found")
        self.assertEqual(task2.full_twenties, 12, 
                        "full_twenties is miscalculated")
        
        self.assertTrue(hasattr(task2, 'remaining_dollars'), 
                       "Variable 'remaining_dollars' not found")
        self.assertEqual(task2.remaining_dollars, 4, 
                        "remaining_dollars is miscalculated")
        
        # Check output format
        expected_output = """Account Holder: Taylor Banks
Remaining Balance: $244
Full $20 Bills: 12
Remaining Dollars: $4
"""
        self.assertEqual(output, expected_output, 
                        "Output format does not match expected format")


if __name__ == '__main__':
    unittest.main()
