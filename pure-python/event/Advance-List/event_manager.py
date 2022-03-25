from typing import Dict, List
from event_interfaces import Listener_Interface


class Event_Manager:
    """
    Event Manager for objects to publish some event to other object
    """

    # describe type hint of var
    listeners: Dict[str, List[Listener_Interface]]
    listeners = dict()

    @staticmethod
    def check_listener(listener: Listener_Interface) -> bool:
        """
        Check the 'listener' object is a sub class of 'Listener_Interface'


        Parameters
        ----------
        listener : Listener_Interface

        Returns
        -------
        bool
            return a boolean due to the type of listener

        """

        if isinstance(listener, Listener_Interface) != True:
            raise TypeError(
                "this listener instance does't inheritance from Listener_Interface"
            )

        return True

    @classmethod
    def add_listener(cls, type_event: str, listener: Listener_Interface) -> None:
        """
        Add a New 'listener' to event listener.

        Parameters
        ----------
        type_event : str
        listener : a instance sub class of Listener_Interface
        """
        if cls.check_listener(listener):
            if type_event in cls.listeners:
                cls.listeners[type_event].append(listener)
            else:
                cls.listeners[type_event] = [listener]

    @classmethod
    def remove_listener(cls, listener: Listener_Interface) -> None:
        """
        Remove a 'listener' of event listener
        """
        cls.listeners.remove(listener)

    def notify(cls, type_event: str, data) -> None:
        """
        Send Notification to a gorup of listener with type event name
        Parameters
        ----------
        type_event: str
        """
        for listener in cls.listeners.get(type_event, []):
            listener.update(data)
