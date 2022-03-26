from typing import Dict, List
from event_interfaces import ListenerInterface


class EventManager:
    # define type hint tf var
    listeners: Dict[str, List[ListenerInterface]]
    listeners = dict()

    @staticmethod
    def check_type_listener(listener: ListenerInterface) -> bool:
        if isinstance(listener, ListenerInterface):
            return True
        return False

    @classmethod
    def add_listener(cls, type_event: str, listener: ListenerInterface) -> bool:

        if cls.check_type_listener(listener) == False:
            return False

        if not type_event in cls.listeners:
            # create a list for key[type_event] to store listeners
            cls.listeners[type_event] = []

        cls.listeners[type_event].append(listener)
        return True

    @classmethod
    def remove_listener(cls, type_event: str, listener: ListenerInterface) -> bool:
        if not type_event in cls.listeners:
            return False
        cls.listeners[type_event].remove(listener)
        return True

    @classmethod
    def notify(cls, type_event: str, data) -> None:
        """sending a notification to all handlers registered to type_event

        Args:
        ----
            type_event (str): target event
            data (Any): pass data to handlers
        """
        # call all handler in a group type_event
        for listener in cls.listeners.get(type_event, []):
            listener.update(data)
