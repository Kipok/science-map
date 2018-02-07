from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', home_page, name='home'),
    url(r'^paper/', include('paper.urls')),
] + staticfiles_urlpatterns()
