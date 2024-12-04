"""
URL configuration for cc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from collec_management import admin
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.menu, name='menu'),
    path('collection/<int:id>/' , views.collection , name='collection') ,
    path ('new/' , views.new , name='new'),
    path('all/', views.all, name='all'),
    path('delete/<int:collec_id>/' , views.delete , name='delete'),
    path('change/<int:collec_id>/' , views.change , name='change'),
    path('element/<int:id>/' , views.element , name='element') ,
    path('element/edit/<int:id>/' , views.element_edit , name='element_edit') ,

]
