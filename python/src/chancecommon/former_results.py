# import boto3
import re
from . import InvalidResultError

class FormerResults:

    # a sample line is 11/22/2025; 28,32,36,51,69; Powerball: 2
    def __init__(self):
        self._section_pattern = re.compile("(.*);(.*);(.*)")
        self._number_pattern = re.compile(r"(\d+)")
        self._expected_numbers = 5

    def process_result(self, result):
        pass

    def extract_numbers(self, result):
        sections = self._section_pattern.match(result)
        if not sections:
            raise InvalidResultError(result)

        try:
            numbers_sections = sections.group(2)
            numbers = [int(number_text) for number_text in self._number_pattern.findall(numbers_sections)]
            if len(numbers) != self._expected_numbers:
                raise InvalidResultError(result)
            lucky_number = int(self._number_pattern.findall(sections.group(3))[0])
        except Exception:
            raise InvalidResultError(result)
        else:
            return [numbers, lucky_number]

    def update_match_frequency(self, number):
        pass
