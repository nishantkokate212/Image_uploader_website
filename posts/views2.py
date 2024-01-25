from django.shortcuts import render,redirect
from .forms import PostsForm
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(req):
    
    return render(req,"index.html")

def home(req):
    id =req.user.id
    print(id)
    photos=Posts.objects.filter(id=id)
    context={"photos":photos,"id":id}
    return render(req,"home.html",context)

def upload(req):
    if req.user.is_anonymous:
        return redirect("/log_in")
    return render(req,"upload.html")

def upload_photo(req):
    if req.method == "GET":
        return render(req,"upload.html")
    else:
        caption=req.POST["caption"]
        photo=req.FILES["photo"]
        context={}
        
        if not(caption and photo):
            context["errmsg"]="All BOXES SHOULD BE FILLED"
            return render(req,"upload.html",context)
        
        else:
            photo=Posts.objects.create(photo=photo,caption=caption)
            photo.save()
            return redirect("/home")
    
    
def sign_up(req):
    if req.method == "POST":
        uname=req.POST.get('uname')
        uemail=req.POST.get('uemail')
        upass=req.POST.get('upass')
        ucpass=req.POST.get('ucpass')
        context={}

        if not(uname and uemail and upass and ucpass):
            context["errmsg"]="Please fill all the credentials!"
            return render(req,"sign_up.html",context)
        elif upass!=ucpass:
            context["errmsg"]="Please match the password!"
            return render(req,"sign_up.html",context)
        elif User.objects.filter(email=uemail).exists():
            context["errmsg"]="Email is already registered, Try with new email!"
            return render(req,"sign_up.html",context)
        else:
            user_obj=User.objects.create_user(uname,uemail,upass)
            user_obj.save()
            return redirect("/log_in")
        
    return render(req,"sign_up.html")

def log_in(req):
    if req.method == 'POST':
        uname=req.POST.get("uname")
        upass=req.POST.get("upass")
        context={}
        user_obj = authenticate(req,username=uname, password=upass)
        print(uname,upass)
        if not(uname and upass):
            context["errmsg"]="Please fill all the credentials!"
            return render(req,'log_in.html',context)
        elif user_obj is not None:
            login(req,user_obj)
            return redirect("home")
        else:
            context["errmsg"]="username or password is incorrect!"
            return render(req,"log_in.html",context)
        
    return render(req,"log_in.html")


    #     if not(uname and upass):
    #         context["errmsg"]="Please fill the all boxes!"
    #     else:
    #         user=authenticate(uname=uname, upass=upass)
    #         login(req,user)
            
    #         return redirect("/home")
    return render(req,"log_in.html")

def log_out(req):
    logout(req)
    return redirect("/log_in")
    
def footer(req):
    return render(req,"footer.html")



