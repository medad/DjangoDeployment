from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('other', views.other, name='basic_app_other'),
    path('relative', views.relative, name='basic_app_relative'),
]

