from typing import Dict


class EventManager:
    listeners: Dict[str, object]
