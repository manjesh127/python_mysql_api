from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello , name = "home"),
    path('save_detail/',views.insertApi , name = 'api'),
    path('getApi/',views.getApi , name = 'register'),
    path('login/',views.emplyLogin , name = 'login'),
    path('verify/',views.verifyLogin , name = 'check'),
]