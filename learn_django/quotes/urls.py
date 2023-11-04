from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<str:author>', views.author, name='author'),   
    path('create/author', views.CreateAuthorView.as_view(), name='create_author'),    
    path('create/quote', views.create_quote, name='create_quote'),
]
