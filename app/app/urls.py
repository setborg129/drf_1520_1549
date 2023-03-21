"""todo URL Configuration

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
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from users.views import UserSerializers, BiographyViewSet, BookViewSet
from TODO.views import ToDoViewSet, ProjectViewSet
# from app.users.views import UserSerializers, BiographyViewSet, BookViewSet
route = DefaultRouter()
route.register('users', UserSerializers)
route.register('Biography', BiographyViewSet)
route.register('books', BookViewSet)

route.register('TODO', ToDoViewSet)
route.register('Project', ProjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api_', include(route.urls)),
]
