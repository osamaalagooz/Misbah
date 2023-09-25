"""
Base OutputParser class

OutputParsers are used to modify the code before it is executed.
"""

from abc import ABC, abstractmethod

from core_ai.exceptions import MethodNotImplementedError


class OutputParser(ABC):
    """Base OutputParser class"""

    _has_run: str = False

    @abstractmethod
    def run(self, code: str) -> str:
        """Run the OutputParser"""
        raise MethodNotImplementedError

    def __call__(self, code) -> str:
        """Call the OutputParser"""
        self._has_run = True
        return self.run(code=code)

    @property
    def has_run(self) -> bool:
        """Return if the OutputParser has run"""
        return self._has_run
