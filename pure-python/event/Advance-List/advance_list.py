from event_manager import Event_Manager


class advance_list(list):
    """
    advance list its a list can be monitor via other objects in realtime
    """

    def __init__(self, *args, **kwargs):
        self.event_manager = Event_Manager()

        return super().__init__(*args, **kwargs)

    def __setitem__(self, index, object):
        """
        Update item with index
        """

        self.event_manager.notify("update-item", (index, object, self))
        return super().__setitem__(index, object)

    def append(self, object):
        """
        Append new item to advance list
        """

        self.event_manager.notify("append-item", self)
        return super().append(object)
