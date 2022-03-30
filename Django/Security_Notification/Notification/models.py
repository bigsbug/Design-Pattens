from typing import Iterable, Optional
from django.contrib.auth.models import User
from django.db import models
from Notification.EventSystem.evnet_manager import EventManager

evnet_manager = EventManager()

# class Subscriber_Group_Name(models.Model):
#     name = models.CharField(
#         verbose_name="Group Name", max_length=21, primary_key=True, unique=True
#     )

#     class Meta:
#         verbose_name = "Subscriber Group"
#         verbose_name_plural = "Subscriber Groups"


# class Subscriber_Group(models.Model):
#     group = models.ForeignKey(
#         Subscriber_Group_Name, models.CASCADE, related_name="Subscriber_Group"
#     )
#     uesrs = models.ManyToManyField(User, related_name="Subscriber_Group")

#     class Meta:
#         verbose_name = "Subscriber"
#         verbose_name_plural = "Subscribers"


class CustomModel(models.Model):
    my_field = models.CharField(max_length=22)

    def save(self, *args, **kwargs):
        evnet_manager.notify("post_save", self)
        super(CustomModel, self).save(*args, **kwargs)
