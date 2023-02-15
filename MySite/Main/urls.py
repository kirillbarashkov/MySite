from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),  # http://127.0.0.1:8000/
    # path('projects/<int:project_id>/', projects),  # http://127.0.0.1:8000/projects/1/
    path('projects/<slug:project_name>/', projects),  # http://127.0.0.1:8000/projects/majicball/
]
