from django.apps import AppConfig


class NormalappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "NormalApp"

    def ready(self) -> None:
        from NormalApp import model_signals
