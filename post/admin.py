from django.contrib import admin
from .models import Post
#   from post.models import Post # Same things with above


class PostAdmin(admin.ModelAdmin):

    list_display = ['id','title', 'publishDate']
    list_display_links = ['title','publishDate']
    list_filter = ['publishDate']
    search_fields = ['title', 'content']
    # list_editable = ['title'] The value of 'title' cannot be in both 'list_editable' and 'list_display_links'.
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)