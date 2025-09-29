from abc import ABC, abstractmethod


class Operation(ABC):

    def __init__(self, *operands):
        self.operands = operands

    @abstractmethod
    def execute(self):
        pass
