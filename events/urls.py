import os
from django.contrib import admin
from django.urls import path
from events import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('hackathons', views.hackathons),
    path('webinars', views.webinars),
    path('fests', views.fests),
    path('seminars', views.seminars),
    path('case_studies', views.case_studies),
    path('debates', views.debates),  

    path('fests/<int:myid>', views.fest_page),
    path('webinars/<int:myid>', views.fest_page),
    path('seminars/<int:myid>', views.fest_page),
    
    path('case_studys/<int:myid>', views.hackathon_page),
    path('debates/<int:myid>', views.hackathon_page),
    path('hackathons/<int:myid>', views.hackathon_page),

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  