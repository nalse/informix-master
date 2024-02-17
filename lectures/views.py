from django.shortcuts import render, get_object_or_404
from .models import Lecture
from pages.models import Pages
from contact.models import Contact
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contact.models import ContactLecture
# Create your views here.
def index(request):
    lectures = Lecture.objects.all()
    pages =Pages.objects.last()
    paginator = Paginator(lectures,8)
    page = request.GET.get('page',2)
    paged_lectures = paginator.get_page(page)
    content = {
        "lectures" : paged_lectures,
        "pages" : pages
    }
    return render(request, "kateqoriya/lectures.html", content)

def lecture(request, lecture_id):
    lectures = Lecture.objects.exclude(id=lecture_id)
    lecture = get_object_or_404(Lecture, pk= lecture_id)
    pages = Pages.objects.last()
    mesajlar = ContactLecture.objects.filter(lecture_id= lecture.id  )
    content = {
        'mesajlar':mesajlar,
        'lecture':lecture,
        "lectures":lectures,
        'pages':pages,
    }
    return render (request,'kateqoriya/lecture.html',content)