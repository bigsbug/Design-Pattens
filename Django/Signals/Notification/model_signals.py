from Notification.EventSystem.evnet_manager import EventManager
from Notification.EventSystem.event_interfaces import ListenerInterface

event_manager = EventManager()


class PostSave_CustomModel(ListenerInterface):
    def update(self, sender):
        print('log : a post saved in "CustomModel"')


event_manager.add_listener("post_save", PostSave_CustomModel())
