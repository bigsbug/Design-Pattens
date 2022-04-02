from django.contrib import admin
from NormalApp.models import NormalModel


@admin.register(NormalModel)
class Rigister_NormalModel(admin.ModelAdmin):
    pass
