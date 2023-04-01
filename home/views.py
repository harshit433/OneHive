from django.shortcuts import render, HttpResponse

from home.models import contact

context = {
    'variable1':contact.objects.all().values()
}

def home(request):
    if request.method == "POST":
        username = request.POST['emailID']
        key = request.POST['PASS']

        result = contact(email = username, password = key)
        result.save()
    
    return render(request,'index.html',context)

def about(request):
    return HttpResponse('this is about page.')
