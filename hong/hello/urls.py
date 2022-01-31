from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('question', views.question, name = 'question'),
    path('home', views.home, name='home'),
    path('about', views.about, name = 'about'),
    path('greet', views.greet, name = 'greet'),
    path('greeting',views.greeting, name = 'greeting'),
    path('great', views.great, name = 'great' ),
]