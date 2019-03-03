from . import views
from django.urls import path, include

app_name='myblog'

urlpatterns = [
    path('', views.index, name="index"),
]