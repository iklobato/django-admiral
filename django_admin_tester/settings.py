from django.conf import settings


class AdminTesterSettings:

    @property
    def WAIT_TIMEOUT(self):
        return getattr(settings, 'ADMIN_TESTER_WAIT_TIMEOUT', 10)

    @property
    def IMPLICIT_WAIT(self):
        return getattr(settings, 'ADMIN_TESTER_IMPLICIT_WAIT', 10)

    @property
    def BROWSER(self):
        return getattr(settings, 'ADMIN_TESTER_BROWSER', 'chrome')

    @property
    def HEADLESS(self):
        return getattr(settings, 'ADMIN_TESTER_HEADLESS', True)

    @property
    def WINDOW_SIZE(self):
        return getattr(settings, 'ADMIN_TESTER_WINDOW_SIZE', (1920, 1080))

    @property
    def SCREENSHOT_ON_FAILURE(self):
        return getattr(settings, 'ADMIN_TESTER_SCREENSHOT_ON_FAILURE', True)

    @property
    def SCREENSHOT_DIR(self):
        return getattr(settings, 'ADMIN_TESTER_SCREENSHOT_DIR', None)

    @property
    def DEFAULT_ADMIN_USERNAME(self):
        return getattr(settings, 'ADMIN_TESTER_DEFAULT_ADMIN_USERNAME', 'admin')

    @property
    def DEFAULT_ADMIN_EMAIL(self):
        return getattr(
            settings, 'ADMIN_TESTER_DEFAULT_ADMIN_EMAIL', 'admin@example.com'
        )

    @property
    def DEFAULT_ADMIN_PASSWORD(self):
        return getattr(settings, 'ADMIN_TESTER_DEFAULT_ADMIN_PASSWORD', 'admin123')

    @property
    def CUSTOM_WAIT_CONDITIONS(self):
        return getattr(settings, 'ADMIN_TESTER_CUSTOM_WAIT_CONDITIONS', {})


admin_tester_settings = AdminTesterSettings()

