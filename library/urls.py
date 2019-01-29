"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from books import views
from profiles import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', include('books.urls')),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
]

urlpatterns += [
    path('profiles', profile_views.profile_list, name='profile_list'),
    path('profiles/create/', profile_views.profile_create, name='profile_create'),
    path('profiles/<int:pk>/update', profile_views.profile_update, name='profile_update'),
    path('profiles/<int:pk>/delete/', profile_views.profile_delete, name='profile_delete'),
]