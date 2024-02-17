from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('videos/',include('videos.urls')),
    path('lectures/',include('lectures.urls')),
    path('quizes/',include('quizes.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/',include('account.urls')),
    path('contact/',include('contact.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/reset_password.html',html_email_template_name='account/password_reset_email.html'), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='account/reset_password_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/reset.html'), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='account/reset_password_complate.html'), name="password_reset_complete"), 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'pages.views.handling_404'

