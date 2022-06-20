from django.contrib import admin
from .models import user_profile,Interset,Friend_request
# Register your models here.
admin.site.register((user_profile,Interset,Friend_request))
