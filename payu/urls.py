from django.conf.urls import url, include

app_name = 'payu'
urlpatterns = [
    url(r'^api/', include('payu.urls_api', namespace='api'))
]
