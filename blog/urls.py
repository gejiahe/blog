
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('index/',views.index,name='index'),
    path('archive/',views.archive,name='archive'),
    path('article/',views.article,name='article'),

    path(r'logout/', views.do_logout, name='logout'),
    path(r'reg/', views.do_reg, name='reg'),
    path(r'login/', views.do_login, name='login'),
    path(r'comment/post/', views.comment_post, name='comment_post'),
]
