import event_handler
from advance_list import advance_list

# Setup Handlers
event_handler.Setup_Alert_Handler()
event_handler.Setup_Logger_Handler()

newlist = advance_list([1241, 2, 3])
newlist.append(132)
newlist[3] = 12_00
