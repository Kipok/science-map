from django.urls import path
from . import views

app_name = 'paper'
urlpatterns = [
    path('<int:paper_id>/', views.paper_view, name='paper'),
    # path('<int:method_id>/', views.method_view, name='method'),
]
