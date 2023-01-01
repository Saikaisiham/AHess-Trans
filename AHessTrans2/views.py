from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Users,Post,Comment,ChatMsg
from .forms import SettingsForm,CommentForm,MessageForm,PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="/password/password_reset.html", context={"password_reset_form":password_reset_form})


def index(request):
    return render(request, 'index.html')


def messages(request,pk):
    other_user =  User.objects.get(id=pk)
    user = request.user
    reciever = User.objects.get(id=other_user.id)
    

    form = MessageForm()
    if request.method == 'POST' :
        form = MessageForm(request.POST)
        if form.is_valid():
            messages = form.save(commit=False)
            messages.sender = user
            messages.reciever = reciever
            messages.seen = True
            messages.save()

    context = {
        'form' : form
    }

    return render(request,'chat.html',context)


@login_required(login_url='/login/')
def Writecomment(request,pk):

    post = Post.objects.get(id=pk) 

    if request.method == 'POST' : 
        comment = Comment.objects.create(
            user = request.user,
            post = post ,
            body = request.POST['body']
        )
        
    
    
    return render(request, 'comment_section.html')

@login_required(login_url='/login/')
def base(request):
    post  =  Post.objects.all()
    comment = Comment.objects.all()
    messages =  ChatMsg.objects.all()  
    user = User.objects.all()

    if request.method == 'POST':
        post_upload = Post.objects.create(
            host = request.user,
            image = request.FILES.get('image_upload'),
            description = request.POST['desc']
            
            )

    context = {
        'post' : post,
        'comment' : comment,
        'messages' : messages,
        'user' : user,
        
 
    }
    return render(request,'base.html',context)

def login(request):

    page ='login'

    if request.method == 'POST' :
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try : 
            user = User.objects.get(username=username)
        except :
            messages.error(request, "User doesn't exist")
        
        user = authenticate(request,username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('/base/')
        else : 
            messages.error(request, "Username or password doesn't exist ")


    context ={
        'page' : page
    }

    return render(request, 'auth/login_register.html',context)



def register(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST' : 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =  form.save()
            user.username = user.username.lower()
            
            user.save()
            auth.login(request,user)
            return redirect('/settings/')
        else : 
            messages.error(request,'An error accured durig registration')

    context = {
        'page' : page
        , 'form' : form
    }

    return render(request,'auth/login_register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('/')



def settingsProfile(request):

    profile = Users.objects.get(user=request.user)
    form = SettingsForm(instance=profile)

    if request.method == 'POST' : 
        form = SettingsForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/settings/')

    context = {
        'form' : form
    }
    
    return render(request,'settings.html',context)


def about(request):
    return render(request, 'about.html')

def post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/base/')
    
    context = {
        'form' : form
    }
    return render(request, 'base.html',context)

