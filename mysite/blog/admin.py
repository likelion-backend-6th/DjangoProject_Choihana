from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','publish','status')
    list_filter = ('publish',)
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','body')
    list_filter = ('created','updated','active')
    search_fields = ('name','email','body')

