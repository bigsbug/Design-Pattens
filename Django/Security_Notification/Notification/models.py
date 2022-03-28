from django.db import models
from django.contrib.auth.models import User


class Subscriber_Group_Name(models.Model):
    name = models.CharField(
        verbose_name="Group Name", max_length=21, primary_key=True, unique=True
    )

    class Meta:
        verbose_name = "Subscriber Group"
        verbose_name_plural = "Subscriber Groups"


class Subscriber_Group(models.Model):
    group = models.ForeignKey(
        Subscriber_Group_Name, models.CASCADE, related_name="Subscriber_Group"
    )
    uesrs = models.ManyToManyField(User, related_name="Subscriber_Group")

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
