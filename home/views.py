
from django.forms import PasswordInput
from django.shortcuts import render,HttpResponse ,redirect
from home.models import Contact
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Contact 
def index(request):
    con1 = Contact.objects.all()
    #con.name='mayanktamrkar',
    #con.email='mayank@322'
    bookdata = { "details" : con1 }

    return render(request,'index.html',bookdata)

    
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render (request,'signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('index',user)
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')





def about(request):
   
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=Contact(name=name,email=email)
        contact.save()
    return render(request,'contact.html')
  






def logout(request):
    if request.method == 'POST':
        auth.logout(request)
# Create your views here.
