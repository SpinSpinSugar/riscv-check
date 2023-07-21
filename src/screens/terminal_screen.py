"""Module with TerminalScreen"""
from colorama import Fore
from src.screens.iscreen import IScreen
from src.run_tests import TestsManager, Test

class TerminalScreen(IScreen):
    """Class that prints tests results in terminal"""
    tests_manager: TestsManager
    def __init__(self, tests_manager: TestsManager):
        self.tests_manager = tests_manager
    def print(self) -> None:
        """Print tests to terminal"""
        if not self.is_ready():
            raise RuntimeError('Tests not ready')
        for test_group in self.tests_manager.tests_groups:
            print(f'\n{test_group.name}')
            i = 1
            for test in test_group.tests:
                self._print_test(test, i, test.test_name)
                i += 1

            self.tests_manager.total_stat.test_counter += test_group.stats.test_counter
            self.tests_manager.total_stat.passed_counter += test_group.stats.passed_counter
        self.tests_manager.total_stat.print_stats('\nTotal')

    @staticmethod
    def _print_test(test: Test, test_number: int, test_name: str) -> None:
        """Print information about test"""
        if not test.executed:
            raise RuntimeError('Test was not executed before print')
        if test.passed:
            print(Fore.GREEN + f'TEST #{test_number} PASSED: {test_name} is generated')
        else:
            print(Fore.RED + f'TEST #{test_number} FAILED: {test_name} is not supported')

    def is_ready(self) -> bool:
        """Checks if TestsManager is ready to be printed"""
        return self.tests_manager.is_ready()
