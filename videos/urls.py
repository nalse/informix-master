from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name ='videos'),
    path('<int:video_id>',views.video, name='video'),
]