from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'paper'
urlpatterns = [
    path('<int:paper_id>/', views.paper_view, name='paper'),
]
