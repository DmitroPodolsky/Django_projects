
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.menu,name='123'),
    path('<str:hey1>/',views.ranc,name='determination' ),
]