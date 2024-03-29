from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('add_project/', add_project, name='add_project'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]
