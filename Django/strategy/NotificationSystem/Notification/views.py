from django.shortcuts import render
from Notification.notification_interface import StrategyInterface


class Notification:
    strategy: StrategyInterface

    def Notify(self, request, message, toAll=False) -> bool:
        return self.strategy.notify(request, message, toAll)
