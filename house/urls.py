"""Houch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    IdeaView,
    PostListView,
    RentalPostListView,
    PostDetailView,
    RentalPostDetailView,
    PostCreateView,
    PostUpdateView,
    RentalPostUpdateView,
    PostDeleteView,
    UserPostListView,
    UserSavedPostListView,
    SignUpView
)
from .import views
# from users.views import responses
from django.conf.urls import url

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about',SignUpView.as_view(),name='about'),
    path('pricing',TemplateView.as_view(template_name='house/pricing.html'),name='pricing'),

    path('for_sale/<slug:city_slug>/<slug:neighborhood_slug>/', PostListView.as_view(), name='house-home'),
    path('for_rent/<slug:city_slug>/<slug:neighborhood_slug>/', RentalPostListView.as_view(), name='house-home-rental'),

    path('for_sale/<slug:city_slug>/<slug:neighborhood_slug>/<int:pk>/<slug:title_slug>/', PostDetailView.as_view(), name='post-detail'),
    path('for_rent/<slug:city_slug>/<slug:neighborhood_slug>/<int:pk>/<slug:title_slug>/', RentalPostDetailView.as_view(), name='post-detail-rental'),

    path('!post/new/', PostCreateView.as_view(), name='post-create'),
    path('for_sale/<slug:city_slug>/<slug:neighborhood_slug>/<int:pk>/<slug:title_slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('for_rent/<slug:city_slug>/<slug:neighborhood_slug>/<int:pk>/<slug:title_slug>/update/', RentalPostUpdateView.as_view(), name='post-update-rental'),
    
    path('<slug:city_slug>/<slug:neighborhood_slug>/<int:pk>/<slug:title_slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    

]
