from django.conf.urls import url

# callable views
from .api import notify

app_name = 'api'
urlpatterns = [
    url(r'^notify/$', notify, name='notify')
]
