from django.urls import path
from . import views

app_name = 'elements'
urlpatterns = [
  path('paper/<int:paper_id>/', views.paper_view, name='paper'),
  path('method/<int:method_id>/', views.method_view, name='method'),
]
