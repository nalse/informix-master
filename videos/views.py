from django.shortcuts import render, get_object_or_404
from .models import Video
from pages.models import Pages
from teacher.models import Teacher
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from contact.models import Contact
# Create your views here.
def index(request):
    pages = Pages.objects.all().last()
    videos = Video.objects.all() 
    paginator = Paginator(videos,3)
    page = request.GET.get('page',3)
    paged_videos = paginator.get_page(page)
    content = {
        'video': video,
        'videos': paged_videos,
        'pages':pages
    }
    return render(request,'kateqoriya/videos.html', content)

def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    pages = Pages.objects.last()
    videos = Video.objects.exclude(id=video_id)
    mesajlar = Contact.objects.filter(video_id= video.id)
    content = {
        'mesajlar':mesajlar,
        'video': video,
        'videos':videos,
        'pages':pages
    }
    return render(request, 'kateqoriya/video.html', content)

