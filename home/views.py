from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def home(request):
    context = {
        "variable1": "This is variable 1",  
        "variable2": "This is variable 2"
    }
    return render(request, "index.html", context)


    # return HttpResponse("this is homepage")

def same(request):
    return HttpResponse("this is same page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        hone = request.POST.get('phone')
        desc = request.POST.get('desc')
        img = request.POST.get('img')
        
        
        
        contact = Contact(name=name, email=email, phone=hone, desc=desc, date=datetime.today(), img=img)
        contact.save()

        
        
    
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
    
