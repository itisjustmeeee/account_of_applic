from django.apps import AppConfig
from django.db.backends.signals import connection_created
from .search_func import unicode_contains


def register_sqlite_functions(sender, connection, **kwargs):
    if connection.vendor == 'sqlite':
        connection.connection.create_function(
            'unicode_contains',
            2,
            unicode_contains,
        )


class UserRequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_requests'

    def ready(self):
        from . import look_ups

        connection_created.connect(
            register_sqlite_functions,
            dispatch_uid='register_unicode_contains',
        )
