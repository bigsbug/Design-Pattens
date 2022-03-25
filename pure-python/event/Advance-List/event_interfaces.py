from abc import ABC, abstractmethod


class Listener_Interface(ABC):
    """an interface for all Listerner Event"""

    @abstractmethod
    def update(self, data):
        """the update method call every time an event happend

        Args:
            data (Any): Required data in listener handler.
        """
        pass
