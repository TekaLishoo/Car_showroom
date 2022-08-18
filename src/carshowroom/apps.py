from django.apps import AppConfig


class CarshowroomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.carshowroom"

    def ready(self):
        import src.carshowroom.signals
