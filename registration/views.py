from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from registration.models import student #hapa unaweka majina ya models zako
def registration(request):
    return HttpResponse("welcome to enrollment")
def mypage(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())



@csrf_exempt
# Create your views here.
def addstudent(request):
    if request.method == 'POST':
       name = request.POST.get('studname')
       age = request.POST.get('studage')
       email = request.POST.get('studmail')
       password = request.POST.get('pswd')

       mydata = {'name': name, 'email': email, 'age': age, 'password': password}
       print(mydata)

       object1 = student(name=name,age=age,email=email,password=password)
       object1.save()
   # fetch the student data to be displayed
    data = student.objects.all();
    context = {'data': data}
    return render(request,'dashboard.html', context)

