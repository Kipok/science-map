from django.urls import path
from . import views

app_name = 'elements'
urlpatterns = [
  path('paper/<int:paper_id>/', views.paper_view, name='paper'),
  path('method/<int:method_id>/', views.method_view, name='method'),
  path('dataset/<int:dataset_id>/', views.dataset_view, name='dataset'),
  path('metric/<int:metric_id>/', views.metric_view, name='metric'),
]
