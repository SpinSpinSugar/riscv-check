"""This module checks if the desired asm instruction was generated after compilation"""
import src.dir_manager as dm
from src.tests_manager import TestsManager

def main() -> TestsManager:
    """Collect and run tests"""
    dir_manager = dm.DirManager()
    tests_manager = TestsManager(dir_manager)
    tests_manager.collect_test_groups()
    tests_manager.run()
    return tests_manager

if __name__ == '__main__':
    main()
