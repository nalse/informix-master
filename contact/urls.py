from django.urls import path
from . import views

urlpatterns = [
    path('contact',views.contact, name ='contact'),
    path('contact_lecture',views.contact_lecture, name ='contact_lecture'),
]