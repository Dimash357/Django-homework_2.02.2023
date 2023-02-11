from django.urls import path
from django_app import views

app_name = 'django_app'

urlpatterns = [
    path('', views.home_view, name=''),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post_create/', views.post_create, name='post_create'),
]