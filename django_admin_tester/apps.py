from django.apps import AppConfig
from django.conf import settings


class DjangoAdminTesterConfig(AppConfig):
    name = 'django_admin_tester'
    verbose_name = 'Django Admin Tester'

    def ready(self):
        # Import signal handlers
        from . import signals

        # Register default settings
        self.register_default_settings()

    def register_default_settings(self):
        """Register default settings for the app."""
        defaults = {
            'ADMIN_TESTER_WAIT_TIMEOUT': 10,
            'ADMIN_TESTER_IMPLICIT_WAIT': 10,
            'ADMIN_TESTER_BROWSER': 'chrome',
            'ADMIN_TESTER_HEADLESS': True,
            'ADMIN_TESTER_WINDOW_SIZE': (1920, 1080),
            'ADMIN_TESTER_SCREENSHOT_ON_FAILURE': True,
            'ADMIN_TESTER_SCREENSHOT_DIR': None,
            'ADMIN_TESTER_DEFAULT_ADMIN_USERNAME': 'admin',
            'ADMIN_TESTER_DEFAULT_ADMIN_EMAIL': 'admin@example.com',
            'ADMIN_TESTER_DEFAULT_ADMIN_PASSWORD': 'admin123',
            'ADMIN_TESTER_CUSTOM_WAIT_CONDITIONS': {},
        }

        for key, default_value in defaults.items():
            if not hasattr(settings, key):
                setattr(settings, key, default_value)
