from django.contrib import admin

# Register your models here.
from .models import Persons

admin.site.register(Persons)

#from .get_by_id import get_by_id

# admin.site.register(Get_by_id)