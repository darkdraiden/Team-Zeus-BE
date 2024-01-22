from django.contrib import admin
from Home.models import User,Board,Task
# Register your models here.
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Task)