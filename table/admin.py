from django.contrib import admin

# Register your models here.
from .models import Typeofbuy, Typeofincome

admin.site.register(Typeofbuy)
admin.site.register(Typeofincome)