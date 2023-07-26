from django.contrib import admin

from blog.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','publish','status')
    list_filter = ('publish',)
    search_fields = ('title',)


