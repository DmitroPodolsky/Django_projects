"""ford URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
admin.site.site_header = 'привет бро'
admin.site.index_title = 'лол я тут'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sql_start.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
]
# '' - сразу переходим по ссылке
# инфа за админкку
#Python manage.py createsuperuser - создание пользователя, находиться в бд auth.user
#на компе клава не отображается при введении пароля, запомни, твой пароль: lolka
