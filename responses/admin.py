from django.contrib import admin
from .models import Response

class ResponseAdmin(admin.ModelAdmin):
    post_display = ('id','name','post','email','contact_date')
    post_display_links = ('id','name')
    search_fields = ('name','email','post')
    post_per_page = 25

admin.site.register(Response, ResponseAdmin)