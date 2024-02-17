from django.urls import path 
from . import views 



urlpatterns = [
    path('',views.quizes, name="quizes"),
    path('<int:pk>/',views.quiz, name="quiz"),
    path('<int:pk>/data/',views.quiz_data_view, name="quiz_data_view"),
    path('<int:pk>/save/',views.save_quiz_view, name="save-view"),
    path('quiz-search/',views.quiz_search, name="quiz-search"),
     

]