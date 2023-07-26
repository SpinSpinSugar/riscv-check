"""Module for TestsManager class"""
import os
import re
from dataclasses import dataclass
from src import dir_manager as dm

@dataclass
class Statistics:
    """Statistics counter"""
    test_counter: int = 0
    passed_counter: int = 0
    def print_stats(self, name: str) -> None:
        """Printing stats with name"""
        print(f'{name}: Passed {self.passed_counter}/{self.test_counter} tests')


class Test:
    """Single test text with info"""
    content: str = ''
    ext: str = ''
    passed: bool = False
    test_name: str = ''
    instr_name: str = ''
    executed: bool = False

    def __init__(self, path: str, ext_name: str, test_name: str, instr_name: str):
        with open(path, 'r', encoding='utf-8') as file_descriptor:
            self.content = file_descriptor.read()
        self.ext = ext_name
        self.test_name = test_name
        self.instr_name = instr_name

    def run_test(self) -> None:
        """Run test and return passed or not, set the passed field"""
        label_begin = self.content.find('test:')
        label_end = self.content.find('ret')
        text = self.content[label_begin:label_end:1]

        instr_pos = re.search(rf'\s{self.instr_name}\s', text)
        if instr_pos:
            self.passed = True
        else:
            self.passed = False
        self.executed = True

    def get_result(self) -> bool:
        """Returns true if test is passed, false otherwise. Raises exception executed=false"""
        if not self.executed:
            raise RuntimeError('Test was not executed before check')
        return self.passed


class TestGroup:
    """Class to collect tests corresponding to same instruction"""
    tests: list[Test] = []
    name: str = ''
    stats: Statistics = Statistics()

    def __init__(self, name: str):
        self.tests = []
        self.name = name
        self.stats = Statistics()
    def append_test(self, test: Test) -> None:
        """Adds test to TestGroup"""
        self.tests.append(test)
        self.stats.test_counter += 1
    def run_tests(self) -> None:
        """Run all tests in TestGroup"""
        for test in self.tests:
            test.run_test()
            result = test.get_result()
            if result:
                self.stats.passed_counter += 1


class TestsManager:
    """Main class to run tests"""
    tests_groups: list[TestGroup]
    dir_manager: dm.DirManager
    total_stat: Statistics
    ready: bool

    def __init__(self, dir_man: dm.DirManager):
        self.tests_groups = []
        self.dir_manager = dir_man
        self.total_stat = Statistics()
        self.ready = False
    def collect_test_groups(self) -> None:
        """Generates TestGroups from directories"""
        prev_dir = self.dir_manager.current_dir
        self.dir_manager.chdir(self.dir_manager.tmp_dir)
        ext_list = os.listdir(self.dir_manager.tmp_dir)
        for ext_dir in ext_list:
            instr_dir_list = os.listdir(ext_dir)
            for instr_dir in instr_dir_list:
                tests_list = os.listdir(f'{ext_dir}/{instr_dir}')
                test_number = 0
                test_group = TestGroup(instr_dir)
                for file in tests_list:
                    test_number += 1
                    command_name = file.removesuffix('.s')
                    test = Test(f'{ext_dir}/{instr_dir}/{command_name}.s',
                                ext_dir,
                                command_name,
                                instr_dir)
                    test_group.append_test(test)
                self.tests_groups.append(test_group)
        self.dir_manager.chdir(prev_dir)

    def run(self) -> None:
        """Runs all tests in all TestsGroups"""
        for test_group in self.tests_groups:
            test_group.run_tests()
        self.ready = True

    def is_ready(self) -> bool:
        """Checks if tests were run"""
        return self.ready
