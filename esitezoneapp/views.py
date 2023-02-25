from django.shortcuts import render
from.models import contact

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        phone = request.POST.get('phone', "")
        email = request.POST.get('email', "")
        massage = request.POST.get('massage', "")

        Contact = contact(name=name, phone=phone, email=email, massage=massage)
        Contact.save()
    return render(request, 'esitezoneapp/index.html')

def blog(request):
    return render(request, 'esitezoneapp/blog.html')

def contactpage(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        phone = request.POST.get('phone',"")
        email = request.POST.get('email',"")
        massage = request.POST.get('massage',"")

        Contact = contact(name=name,phone=phone,email=email,massage=massage)
        Contact.save()
    return render(request, 'esitezoneapp/contact.html')

def elements(request):
    return render(request, 'esitezoneapp/elements.html')

def protfolio(request):
    return render(request, 'esitezoneapp/portfolio.html')

def service(request):
    return render(request, 'esitezoneapp/service.html')

def single_blog(request):
    return render(request, 'esitezoneapp/single-blog.html')

def about(request):
    return render(request, 'esitezoneapp/about-us.html')


def contact_us(request):

    return render(request,'esitezoneapp/index.html')