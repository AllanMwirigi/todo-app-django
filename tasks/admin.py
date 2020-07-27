from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Task) # so that it comes up in the admin page