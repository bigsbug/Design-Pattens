from django.contrib import admin

from Notification.models import CustomModel


@admin.register(CustomModel)
class Register_CustomModel(admin.ModelAdmin):
    pass
