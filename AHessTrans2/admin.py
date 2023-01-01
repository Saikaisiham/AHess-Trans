from django.contrib import admin
from .models import Users,Comment,Post,ChatMsg

# Register your models here.

admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(ChatMsg)

