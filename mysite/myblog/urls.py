from . import views
from django.urls import path, include

app_name='myblog'

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<int:pk>/', views.post, name="post"),
    path('write/', views.write, name="write"),
    path('write/<int:pk>/', views.modi, name="modi"),
    path('del/<int:pk>/', views.delete, name="delete"),
]