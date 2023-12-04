from django.shortcuts import render ,redirect
from.models import *
from django.contrib import messages
import bcrypt
def form(request):
    return render(request ,'index.html')
def registaration(request):
    errors=User.objects.basic_valedater(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password=request.POST['pass']
        pw=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        usr=User.objects.create(first=request.POST['fname'],last=request.POST['lname'],email=request.POST['email'],password=pw)
        request.session['name']=request.POST['fname']
        request.session['id']=usr.id
        return redirect('/sucses')
    
def sucsesregestration(request):
    if 'id' not in request.session:
        messages.errors(request ,"you must log in first !")
        return redirect ("/")
    return render(request,'suc.html')

def logout(request):
    request.session.flush()
    return redirect("/")
def login(request):
    user=User.objects.filter(email=request.POST['email'])
    if user:
        loguser=user[0]
        if bcrypt.checkpw(request.POST['pass'].encode(), loguser.password.encode()):
            request.session['id']=loguser.id 
            request.session['name']=loguser.first
            return redirect('/sucses')
        else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")
    else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")

# Create your views here.
