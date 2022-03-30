from django.db import models


class NormalModel(models.Model):
    normal_field = models.TextField(max_length=22)
