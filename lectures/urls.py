from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name ='lectures'),
    path('<int:lecture_id>',views.lecture, name="lecture")
]