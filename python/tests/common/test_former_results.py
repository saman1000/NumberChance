import unittest

from chancecommon import InvalidResultError
from chancecommon.former_results import FormerResults


class TestFormerResults(unittest.TestCase):

    def test_extract_numbers_valid_text(self):
        test_cases = [
            ('11/22/2025; 28,32,36,51,69; Powerball: 2', [28, 32, 36, 51, 69], 2),
            ('11/22/2025;28,32 ,36, 51,69; Powerball: 24', [28, 32, 36, 51, 69], 24)
        ]
        former_results = FormerResults()
        for result, numbers, lucky_number in test_cases:
            actual = former_results.extract_numbers(result)
            self.assertListEqual(actual[0], numbers)
            self.assertEqual(actual[1], lucky_number)

    def test_extract_numbers_invalid_result(self):
        test_cases = [
            'This is a test',
            '11/22/2025; 28,32,36,51,69; Powerball: ',
            '11/22/2025; ; Powerball: 1',
            '11/22/2025; 28,32,36,51; Powerball: 2'
        ]
        former_results = FormerResults()
        for invalid_result in test_cases:
            with self.assertRaises(InvalidResultError):
                former_results.extract_numbers(invalid_result)
