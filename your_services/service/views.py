from django import forms
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponseRedirect, request
from django.http import HttpResponse
from .models import Post,Querry,likee,slider
from service.utils import avarage_rating,page_devider
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import nameForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from io import BytesIO
from django.urls import reverse

from PIL import Image


from django.core.files.images import ImageFile

def mysearch(request):
    if request.method=="POST":
        print(True)
        content=request.POST['mysearch']
        search_post=Post.objects.filter(title__contains=content)
        result={}
        result['my_post']=search_post
    return render(request,'home.html',result)

# Create your views here.
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    return render("/")

def index(request):
    user_id=request.user.id
    my_post=Post.objects.all().order_by('-liked')
    slide=slider.objects.all()
  

    
    context={
        'my_post':my_post,
        'slider':slide
        
    }
    return render(request,'home.html',context)
    


def post_list(request):
    pass
    

def my_post(request):
    current_user = request.user
    print(current_user.id)
    
    return render(request,'addservice.html')


def posts_detail(request,pk):
    user=[]
    context={}
    post=get_object_or_404(Post,pk=pk)
    userr=User.objects.filter(id=post.creator_id)
    
  
    if post.likes.filter(id=request.user.id).exists():
            like=True
    else:
        like=False
    querys=post.querry_set.all()
    if post.creator_id==request.user.id:
        
        context={
                'post':post,
                'querrys':querys,
                'hider':True,
                'userr':userr[0],
                'like':like
            
                    }
            
            
    else:
        context={
                'post':post,
                'querrys':querys,
                'like':True,
                'hider':False,
                'userr':userr[0],
                'like':like
            
                        }
        
    return render(request,'detail.html',context)






def regis(request):
    return render(request,'register.html')

def ruff(request):
    messages.success(request,"Your account has been successfully created")
    return render(request,'rufff.html')


def handleSignup(request):
    if request.method=='POST':
        #Get all parameter
        username=request.POST.get('username',False)
        firstname=request.POST.get('firstname',False)
        lastname=request.POST.get('lastname',False)
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        pass2=request.POST.get('pass2',False)
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username allready exist try another one")
            return redirect("/")
        elif password!=pass2:
            messages.error(request,"password did not matched")
            return redirect("/")
        elif len(password)<8:
            messages.info(request,"Password should atleast 8 number or charater ")
            return redirect("/")
        else:
            user = User.objects.create_user(username,
                                 email,
                                 password)    
        user.first_name=firstname
        user.last_name=lastname
        user.email=email
        user.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
        #Get all parameter
        loginusername=request.POST['logusername']
        loginpassword=request.POST['logpassword']

        user= authenticate(username=loginusername,
        password=loginpassword)

        if user is not None:
            login(request, user)

            messages.success(request,"Login successfully")
            return redirect("/")
        else:
            messages.error(request,"Somthing wrong please try again")
            return redirect("/")


    return HttpResponse('404 page not fount')
    
def handleLogout(request):
    current_user = request.user
    print(current_user.id)

    logout(request)
    messages.success(request,"suucefully logged Out")
    return redirect("/")

        




def new_service(request):
    return render(request,"home.html")

   
   
def add_service(request):
        if request.method == "POST":
            form = nameForm(request.POST,request.FILES)
            
            if form.is_valid():

                data=form.save(False)
                cover = form.cleaned_data['cover']
                form.instance.creator_id=request.user.id
                

                if cover:
                    print(True)
                    image = Image.open(cover)
                    image.thumbnail((300, 300))
                    image_data = BytesIO()
                    image.save(fp=image_data, format=cover.image.format)
                    image_file = ImageFile(image_data)
                    print(image_file)
                    data.cover.save(cover.name, image_file)
                    
                    

                data.save()

                return redirect('home')

        else:
            form = nameForm()
        user_id=request.user.id
        posts=Post.objects.filter(creator_id=request.user.id)
        return render(
            request, "services.html",
            {
                "form": form,
                "is_file_uploaded": True,
                'posts':posts
                
            }
        )

def add_querry(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        #Get all parameter
        loginusername=request.POST['logusername']
        query_add=Querry.objects.create(content=loginusername,provider_id=request.user.id,post_id=post.id)
        query_add.save()
        

    return redirect("/")

def add_ans(request,pk):
    query=get_object_or_404(Querry,pk=pk)
    
    
    
    
    
    if request.method=="POST":
        ans=request.POST['myans']
        Querry.objects.filter(pk=pk).update(Answer=ans)
        
        messages.success(request,"Ans given...")
    return redirect("/")


def show_ans(request,pk):
    query=get_object_or_404(Querry,pk=pk)
    anss=query.answer_set.all()
    number=len(anss)
    context={}
    context['answers']=anss
    context['num']=number

    return render(request,"detail.html",context)


def add_like(request,pk):
    post=get_object_or_404(Post,pk=pk)
    like=int(post.liked)
    l=like+1
    if request.method=="POST":
        like=likee(user_like_id=request.user.id,post_id=pk)
        like.save()
        Post.objects.filter(pk=pk).update(liked=l)
    return redirect("/")

def myprofile(request):
    user=request.user
    print(user)
    content={
        'user':user
    }
    return render(request,"profile.html",content)
        


def add_like(request,pk):
    post=get_object_or_404(Post,pk=pk)
    like=int(post.liked)
    l=like+1
    p=like-1
    if request.method=="POST":
        like=likee(user_like_id=request.user.id,post_id=pk)
        like.save()
        like_flag=False
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            Post.objects.filter(pk=pk).update(liked=p)
            like_flag=False
        else:
            post.likes.add(request.user)
            Post.objects.filter(pk=pk).update(liked=l)
            like_flag=True 
        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))



    