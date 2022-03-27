from django.contrib import admin
from Notification.models import Subscriber_Group_Name, Subscriber_Group

# Register your models here.
@admin.register(Subscriber_Group)
class Register_Subscriber_Group(admin.ModelAdmin):
    pass


@admin.register(Subscriber_Group_Name)
class Register_Subscriber_Group_Name(admin.ModelAdmin):
    pass
