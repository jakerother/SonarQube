# test_sonarqube.py
"""
Tests for SonarQube module.
"""

import unittest
from sonarqube import SonarQube

class TestSonarQube(unittest.TestCase):
    """Test cases for SonarQube class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SonarQube()
        self.assertIsInstance(instance, SonarQube)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SonarQube()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
