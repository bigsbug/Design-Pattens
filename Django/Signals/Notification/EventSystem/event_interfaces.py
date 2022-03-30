from abc import ABC, abstractmethod


class ListenerInterface(ABC):
    @abstractmethod
    def update(self, data):
        ...
