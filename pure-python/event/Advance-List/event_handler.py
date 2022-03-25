from event_interfaces import Listener_Interface
from event_manager import Event_Manager

event_manager = Event_Manager()


class Alert_Handler(Listener_Interface):
    """Alert when Advance-List chaned any time

    Args:
        Listener_Interface (Class): an interface for event handler
    """

    def update(self, data):
        print("Alert Advance-List changed.")


def Setup_Alert_Handler():
    """Register Alert_Handler to event manager with types

    types:
    -----
    'append-item',
    'update-item'
    """
    event_manager.add_listener("append-item", Alert_Handler())
    event_manager.add_listener("update-item", Alert_Handler())


class Logger_Handler_Update(Listener_Interface):
    """Log event update Advance-List

    Args:
        Listener_Interface (class): an interface for event handler
    """

    def update(self, data):
        index = data[0]
        item = data[1]
        result = data[2].copy()  # a copy of orginal list
        result[index] = item  # update copy

        print(f"Log: index {index} of Advance-List Updated to {item} : {result}")


class Logger_Handler_Append(Listener_Interface):
    """Log Appended item to Advance-List

    Args:
        Listener_Interface (class): an interface for event handler
    """

    def update(self, data):
        print(f"Log: Advance-List Updated to {data}")


def Setup_Logger_Handler():
    """Register Logger_Handler_Update and Logger_Handler_Append to event manager with types

    types:
    -----
    'append-item',
    'update-item'
    """
    event_manager.add_listener("append-item", Logger_Handler_Append())
    event_manager.add_listener("update-item", Logger_Handler_Update())
