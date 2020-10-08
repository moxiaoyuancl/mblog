from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)
class PoostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

admin.site.register(Post,PoostAdmin)