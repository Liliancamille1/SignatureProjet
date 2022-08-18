from django.urls import path
from web import views
from web.views import home,entreprise,menu

urlpatterns = [

    path('', home, name="home"),
    path('register', views.register, name='register'),
    path('login', views.logIn, name='login'),
    path('menu',menu,name="menu"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]