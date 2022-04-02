from abc import ABC, abstractclassmethod


class StrategyInterface(ABC):
    @abstractclassmethod
    def calculate(a: int, b: int) -> int:
        pass
