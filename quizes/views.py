from django.shortcuts import render,get_object_or_404
from .models import Quiz
from django.views.generic import ListView
from pages.models import Pages
from contact.models import Contact
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contact.models import ContactLecture
from questions.models import Answer
from questions.models import Question
from django.http import JsonResponse
from results.models import Result
from django.core import serializers
from django.contrib import messages,auth
from pages.choices import kateqoriya, qiymet

# Create your views here.
def quizes(request):  
    quizes = Quiz.objects.all()
    pages =Pages.objects.last()
    return render(request, "kateqoriya/quizes.html", {
        "quizes" :quizes ,      
        "pages":pages,
        "kateqoriya":kateqoriya
       
    })
def quiz(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    quess= Question.objects.all()
    pages =Pages.objects.last()
    results =Result.objects.all()
    return render(request, "kateqoriya/quiz.html", {
        "quizes" :quiz,
        "pages":pages,
        "quess":quess,
        "results":results,
    })
def quiz_search(request):
    queryset_list = Quiz.objects.all().order_by("tarix")
    pages =Pages.objects.all().last()
    
    if 'kateqoriya' in request.GET:
        kateqoriya = request.GET['kateqoriya']
        if kateqoriya:
            queryset_list= queryset_list.filter(kateqoriya__iexact = kateqoriya)

    if 'qiymet' in request.GET: 
        qiymet = request.GET['qiymet']
        if qiymet:
            queryset_list= queryset_list.filter(qiymet__lte = qiymet)
    
    content ={
        "pages":pages,
        "quizes": queryset_list,
        "values":request.GET
    }
    return render(request,"kateqoriya/quizes_search.html", content)


def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk = pk)
    questions = []
    solAns=[]
    img=[]
    sual=[]
    quizAns=[]
    for q in quiz.get_questions():
        answers = []
        solutions =[]
        suallar = []
        solutions.append(q.hell)
        suallar.append(q.sual)
        for a in q.get_answers():
            answers.append(a.text) 
        questions.append({str(q): answers })  
        img.append({"solutions" : solutions}) 
        sual.append({"suallar":suallar})
        solAns.append({str(q.hell):answers})
    return JsonResponse({
      'data': questions,
      'time': quiz.time,
      'data1':img,
      'data2':sual,
      "data3":solAns,
  })
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def save_quiz_view(request, pk):
    if is_ajax(request=request):
        user_id = request.user.id
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            question = Question.objects.get(text = k)
            questions.append(question)
        user = request.user
        quiz =Quiz.objects.get(pk=pk)
        score = 0
        multiplier = 100/quiz.sual_sayi 
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != "":
                question_answers =Answer.objects.filter(question = q)
                for a in question_answers: 
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q):{'correct_answer': correct_answer, 'answered':a_selected}})
            else:
                results.append({str(q):'not answered'})
        score_ = score * multiplier
        if request.user.is_authenticated: 
            has_result = Result.objects.all().filter(u_id=user_id, q_id=quiz.id)
            if  not has_result:
                Result.objects.create(u_id = user_id,q_id=quiz.id, quiz=quiz, user=user, score = score_)     
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed':True, 'score':score_, 'results':results})
        else:
            return JsonResponse({'passed':False, 'score':score_, 'results':results})
   
    return JsonResponse({"text":"works"})



    