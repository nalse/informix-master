from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from teacher.models import Teacher
from videos.models import Video
from lectures.models import Lecture
from quizes.models import Quiz
from pages.choices import kateqoriya
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

from django.shortcuts import render

def handling_404(request, exception):
    return render(request, '404.html')


def index(request):
    global kategoriya
    pages = Pages.objects.all().last()
    lectures =Lecture.objects.all()
    videos = Video.objects.all() 
    paginator = Paginator(videos,6)
    page = request.GET.get('page',1)
    paged_videos = paginator.get_page(page)
    quizes = Quiz.objects.all()
    content = {
        "pages":pages,
        "videos": paged_videos,
        "lectures":lectures,
        "quizes":quizes,
        "kateqoriya":kateqoriya
    }
    return render(request,'pages/index.html',content)

def about(request):
    pages = Pages.objects.all().last()
    teachers = Teacher.objects.all()
    content = {
        "pages":pages,
        "kateqoriya":kateqoriya,
        "teachers":teachers
    }
    return render(request,"pages/about.html",content)

def search(request):
    global kategoriya
    pages = Pages.objects.all().last()
    queryset_list = Video.objects.order_by("tarix")
    lectures = Lecture.objects.order_by("tarix")
    if 'kateqoriya' in request.GET:
        kateqoriya = request.GET['kateqoriya']
        if kateqoriya:
            queryset_list= queryset_list.filter(kateqoriya__iexact = kateqoriya)     
    content = {
        "pages":pages,
        "kateqoriya":kateqoriya,
        "videos": queryset_list,
        "lectures":lectures,
    }
    return render (request,"pages/search.html",content)

