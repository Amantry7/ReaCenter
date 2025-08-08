from django.apps import AppConfig


class SettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.setting'

    def ready(self):
        # Import signal handlers
        try:
            from . import signals  # noqa: F401
        except Exception:
            # Avoid breaking startup if optional deps missing; log if needed
            pass
