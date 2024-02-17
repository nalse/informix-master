from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
    path('register',views.register, name ='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]