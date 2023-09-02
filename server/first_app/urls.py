from django.urls import path, re_path
from first_app import views

urlpatterns = [

    re_path(r'^$', views.index, name='index'),
    re_path(r'^help1/', views.help1, name='help1'),
    re_path(r'^user_page/', views.user_page, name='user_page'),
    re_path(r'^hello-view/', views.HelloApiView.as_view(),),
]