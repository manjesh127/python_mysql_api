from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello , name = "home"),
    path('save_detail/',views.insertApi , name = 'api'),
    path('getApi/',views.getApi , name = 'register'),
    # path('logout/',views.logout , name = 'logout'),
    # path('contact/',views.contact , name = 'contact'),
    # path('about/',views.about , name = 'about'),
    # path('single/',views.single , name = 'single'),
    # path('shop/',views.single , name = 'shop'),
    # path('coming/',views.coming , name = 'coming'),
    # path('register/registerapi',views.registerapi , name = 'registerapi'),
    # path('login/loginapi',views.loginapi,name='loginapi')

]