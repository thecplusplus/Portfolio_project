from django.urls import path
from .import views
from django.urls import include

urlpatterns=[
    path('',views.blog,name="blog"),
    path('<int:blog_id>/',views.details,name="detail"),
    ]