from django.apps import AppConfig

class DjangoAdminTesterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_admin_tester'
    verbose_name = 'Django Admin Tester'
    
    def ready(self):
        from . import signals


