from django.urls import path, re_path
from . import views

urlpatterns=[
    path('register/', views.customUserRegister),
    path('login/',views.login_user),
    path('',views.index, name='index'),
    re_path(r'^profile/(\d+)', views.profile, name='profile'),
]