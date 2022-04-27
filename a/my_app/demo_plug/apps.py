from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs, PluginSettings

from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType


class DemoPlugConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo_plug'



    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'demo_plug',
                PluginURLs.REGEX: '^demo_plug/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }
