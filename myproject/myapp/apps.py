from django.apps import AppConfig


class ContactManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp.contact_manager'
    AppConfig.default = False