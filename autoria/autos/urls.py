from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.auto_list, name='auto_list'),
    path('create/', views.auto_create, name='auto_create'),
    path('<int:pk>/', views.auto_detail, name='auto_detail'),
    path('<int:pk>/update/', views.auto_update, name='auto_update'),
    path('<int:pk>/delete/', views.auto_delete, name='auto_delete'),
    path('<int:pk>/delete/', views.AutoDeleteView.as_view(), name='auto_delete'),
]