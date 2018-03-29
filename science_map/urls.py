from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import home_page

urlpatterns = [
  path('admin/', admin.site.urls),
  url('^$', home_page, name='home'),
  url(r'^elements/', include('elements.urls')),
] + staticfiles_urlpatterns()

# TODO: change license?