import unittest

from chancecommon import InvalidResultError
from chancecommon.former_results import FormerResults

class TestFormerResults(unittest.TestCase):

    def test_extract_numbers_valid_text(self):
        one_result = '11/22/2025; 28,32,36,51,69; Powerball: 2'
        former_results = FormerResults()
        actual = former_results.extract_numbers(one_result)
        self.assertListEqual(actual[0], [28, 32, 36, 51, 69])
        self.assertEqual(actual[1], 2)

    def test_extract_numbers_invalid_text(self):
        invalid_text = 'This is a test'
        former_results = FormerResults()
        with self.assertRaises(InvalidResultError):
            former_results.extract_numbers(invalid_text)

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

#
# if __name__ == '__main__':
#     unittest.main()
