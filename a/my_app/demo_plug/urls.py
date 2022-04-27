
from django.conf.urls import url

from .views import thanks

urlpatterns = [
    url(
        r'^$',
        demoplug,
        name='demoplug',
    ),
]