from django.shortcuts import render
from events.models import allevents
from django.conf import settings
import os
import datetime

media_path = settings.MEDIA_URL
static_path= settings.STATIC_URL  

context = {
    'images' : media_path,
    'static' : static_path
}

# Create your views here.

def home(request):
    if request.method == "POST":
        eventtype = request.POST['eventtype']
        eventname = request.POST['eventName']
        eventvenue = request.POST['eventVenue']
        eventinfo = request.POST['eventInfo']
        bannerimage =  request.FILES['bannerImage']
        print(bannerimage)
        teamsize = request.POST['teamSize']
        deadline = request.POST['deadline']
        eligibility = request.POST['eligibility']
        category = request.POST['category']
        eventdate = request.POST['eventDate']
        info = request.POST['eventInfo2']
        guidlines = request.POST['guidelines']
        rules = request.POST['rules']
        eventimage =request.FILES['eventImage']
        print(eventimage)
        istprize = request.POST['firstPrize']
        secondprize = request.POST['secondPrize']
        thirdprize = request.POST['thirdPrize']
        participation = request.POST['participationPrize']
        contactname = request.POST['contactName']
        contactno = request.POST['contactNumber']
        url = request.POST['referenceWebsite']

        result = allevents(event_type = eventtype, event_name = eventname, event_venue = eventvenue,event_info = eventinfo, banner_image = bannerimage, team_size = teamsize, deadline = deadline, eligibility = eligibility, category = category, event_date = eventdate, info = info, guidlines = guidlines, rules = rules, event_image = eventimage, ist_prize = istprize, second_prize = secondprize, third_prize = thirdprize, participation = participation, contact_name = contactname, contact_no = contactno, reference_url = url)

        result.save()



    context['all_events'] = allevents.objects.all().values()
    current_date = datetime.date.today()

    context['upcoming_events'] = allevents.objects.filter(event_date__gt =current_date)
    context['live_events'] = allevents.objects.filter(event_date =current_date)
    context['completed_events'] = allevents.objects.filter(event_date__lt =current_date)
    return render(request,'events.html',context)

def hackathons(request):
    
    context['all_hacks'] = list(allevents.objects.filter( event_type = 'hackathon' ).values())
    return render(request,'hackathons.html',context)

def hackathon_page(request,myid):
    context['page'] = list(allevents.objects.filter(id = myid).values())[0]
    return render(request,'event-info.html',context)

def fest_page(request,myid):
    context['page'] = list(allevents.objects.filter(id = myid).values())[0]
    print(context['page']['info'])
    return render(request,'event-info-child.html',context)

def fests(request):
    context['all_fests'] = allevents.objects.filter( event_type = 'fest' ).values()
    return render(request,'fest.html',context)

def webinars(request):
    context['all_webs'] = allevents.objects.filter( event_type = 'webinar' ).values()
    return render(request,'webinars.html',context)

def seminars(request):
    context['all_sems'] = allevents.objects.filter( event_type = 'seminar' ).values()
    return render(request,'seminars.html',context)

def case_studies(request):
    context['all_cases'] = allevents.objects.filter( event_type = 'case_study' ).values()
    return render(request,'case-study.html',context)

def debates(request):
    context['all_debates'] = allevents.objects.filter( event_type = 'debate' ).values()
    return render(request,'debates.html',context)

def organize(request):
    return render(request,'organize-form.html')