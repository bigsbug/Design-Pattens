from django.shortcuts import render
from Notification import notification_type as Notify_Type
from Notification.views import Notification


def home(request):
    notify = Notification()
    notify.strategy = Notify_Type.MessageInSite()
    notify.Notify(request, "Welcome to my WebSite")
    del notify
