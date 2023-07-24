"""Module with CSVFormat class"""
import csv
import sys
from src.tests_manager import TestsManager
from src.formats.iformat import IFormat

class CSVFormat(IFormat):
    """Class for csv format output"""
    tests_manager: TestsManager

    def __init__(self, tests_manager: TestsManager):
        self.tests_manager = tests_manager

    def print(self):
        writer = csv.writer(sys.stdout)
        writer.writerow(['NUM', 'ext', 'instr_name','test_name', 'test_status'])
        i = 0
        for test_group in self.tests_manager.tests_groups:
            for test in test_group.tests:
                i += 1
                writer.writerow([i, test.instr_name, test.test_name, test.get_result()])

    def is_ready(self) -> bool:
        return True
