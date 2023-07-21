"""Abstract class for all screens"""
from abc import ABC, abstractmethod
from src.run_tests import TestsManager

class IScreen(ABC):
    """Abstract class for all the screens"""
    tests_manager: TestsManager
    @abstractmethod
    def print(self) -> None:
        """Print tests to screen"""

    @abstractmethod
    def is_ready(self) -> bool:
        """Checks if TestsManager is ready to be printed"""
