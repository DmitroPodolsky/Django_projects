from . import views
from django.urls import path
urlpatterns = [
    path('',views.func,name='hanyo'),
    path('catalog/<slug:han>',views.func1,name='name'),
    path('top_rating/',views.func2,name='lol')
]