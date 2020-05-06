from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'moderated', 'approved')
    list_editable = ('moderated', 'approved')
    list_filter = ('moderated',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
