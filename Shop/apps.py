from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class AppAdminConfig(AdminConfig):
    default_site = 'app.admin.AppAdmin'


class ShopConfig(AppConfig):
    name = 'Shop'
