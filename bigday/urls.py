from django.urls import re_path as url
from django.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('wedding.urls')),
    url(r'^', include('guests.urls')),
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls'))
]
