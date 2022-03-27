from django.db import models
from django.contrib.auth.models import User


class Group_Name_Subscriber(models.Model):
    name = models.CharField(
        verbose_name="Group Name", max_length=21, primary_key=True, unique=True
    )


class Subscriber_Group(models.Model):
    group = models.ForeignKey(
        Group_Name_Subscriber, models.CASCADE, related_name="Subscriber_Group"
    )
    uesrs = models.ManyToManyField(User, related_name="Subscriber_Group")
