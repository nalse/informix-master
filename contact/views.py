from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from .models import ContactLecture

# Create your views here.
def contact(request):
    if request.method=="POST":
        video = request.POST["video"]
        video_id =request.POST['video_id']
        message = request.POST['message']
        istifadeci = request.user
        contact = Contact(video_id =video_id,istifadeci=istifadeci,video=video, message=message)
        contact.save()
        return redirect('/videos/'+video_id)

def contact_lecture(request):
    if request.method== 'POST':
        lecture_id = request.POST['lecture_id']
        message = request.POST['message']
        istifadeci = request.user
        contact_lecture = ContactLecture(lecture_id =lecture_id,istifadeci=istifadeci, message=message)
        contact_lecture.save()
        return redirect('/lectures/'+lecture_id)

