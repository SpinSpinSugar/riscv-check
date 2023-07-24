"""Abstract class for all formats"""
from abc import ABC, abstractmethod

class IFormat(ABC):
    """Abstract class for all the formats"""
    @abstractmethod
    def print(self) -> None:
        """Print tests to screen"""

    @abstractmethod
    def is_ready(self) -> bool:
        """Checks if TestsManager is ready to be printed"""
