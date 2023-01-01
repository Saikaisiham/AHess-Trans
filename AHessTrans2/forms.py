from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Users,Comment,ChatMsg,Post

class UserForm(ModelForm):
    class Meta : 
        model =  User
        fields = ['username','email']



class SettingsForm(ModelForm):
    class Meta:
        model = Users
        fields = ['bio','image','phone','city','cin']


class CommentForm(ModelForm):
    class Meta : 
        model = Comment
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta : 
        model = ChatMsg
        fields = ['body']

class PostForm(ModelForm):
    class Meta :
        model = Post
        fields = '__all__'
        

