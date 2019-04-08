from django.shortcuts import render, HttpResponse, redirect
from apps.users.models import *

def index(request):
    values = User.objects.all().values()
    print(User.objects.all().values())
    return render(request,'users/index.html', {'values':values})

def expanded(request, id):
    currentid = id
    user = User.objects.get(id =currentid)

    return render(request,'users/expanded.html',{'user':user})

def edituser(request, id):
    user = User.objects.get(id=id)
    currentUser = {
        'first': user.first_name,
        'last': user.last_name,
        'email': user.email,
        'id':id
    }
    print(currentUser)

    return render(request,'users/edituser.html',currentUser)
def updater(request, id):
    d = User.objects.get(id=id)
    d.first_name = request.POST['first_name']
    d.last_name = request.POST['last_name']
    d.email = request.POST['email']
    d.save()
    
    print(User.objects.all().values())
    return redirect('/users')
def delete(request, id):
    d = User.objects.get(id=id)
    d.delete()
    
    print(User.objects.all().values())
    return redirect('/users')

def adduser(request):
    
    return render(request,'users/adduser.html')

def create_process(request):
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
    print(User.objects.last())
    id = request.session['id']
    return redirect('/users')
