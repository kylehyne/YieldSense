# test_yieldsense.py
"""
Tests for YieldSense module.
"""

import unittest
from yieldsense import YieldSense

class TestYieldSense(unittest.TestCase):
    """Test cases for YieldSense class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YieldSense()
        self.assertIsInstance(instance, YieldSense)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YieldSense()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
