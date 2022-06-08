from django.urls import path, re_path
from . import views

urlpatterns=[
    path('register/', views.customUserRegister),
    path('login/',views.login_user),
    path('logout',views.logout_user),
    path('',views.index, name='index'),
    re_path(r'^profile/(\d+)', views.profile, name='profile'),
    re_path(r'^look/(\d+)', views.lookup_profile, name='look'),
    path('image/', views.image_request, name = "image"),
    re_path(r'^like/(\d+)', views.like, name = "like_image"),
    re_path(r'^imageView/(\d+)', views.imageView, name = "imageView"),
    re_path(r'^comment/(?P<image_id>\d+)', views.commentAdd, name='comment'),
    path('search/',views.search, name='search'),
    path('newprofile/',views.update_profile,name ='newprofile'),
    re_path(r'^follow/(?P<user_id>\d+)', views.follow, name='follow'),
]