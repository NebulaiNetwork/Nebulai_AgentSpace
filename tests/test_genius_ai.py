"""
Unit tests for ValidatorAgent
"""

import unittest
from agents.validator_agent import ValidatorAgent

class TestValidatorAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ValidatorAgent()

    def test_validate_returns_string(self):
        input_text = "Sample solution"
        result = self.agent.validate(input_text)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
