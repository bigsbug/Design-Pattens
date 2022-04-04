from abc import ABC, abstractclassmethod


class StrategyInterface(ABC):
    @abstractclassmethod
    def notify(self, reqeust, message, toAll) -> bool:
        pass
