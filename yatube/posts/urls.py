from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    path('morning', views.morning_post_view, name='morning_post_view'),
    path('', views.index, name='index'),
]
