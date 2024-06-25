from django.urls import path
from .views import test_color_url

urlpatterns = [
    path('index/',test_color_url, name = 'test_list'),
]