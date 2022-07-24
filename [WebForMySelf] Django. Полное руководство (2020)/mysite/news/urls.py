from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<int:category_id>/', get_category)
]
