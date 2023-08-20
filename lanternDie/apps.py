from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
        

class LanterndieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lanternDie"
