from django.urls import path
from .views import *

urlpatterns = [
    path('tutorials/', tutorial_list, name="list"),
    path('tutorials/<int:pk>', tutorial_detail, name="detail"),
    path('tutorials/published', tutorial_published, name="published")
]


