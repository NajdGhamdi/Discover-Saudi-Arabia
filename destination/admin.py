from django.contrib import admin
from .models import Destination,Event,Site,Comment

# Register your models here.

admin.site.register(Destination)
admin.site.register(Event)
admin.site.register(Site)
admin.site.register(Comment)