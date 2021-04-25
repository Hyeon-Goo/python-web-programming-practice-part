from django.contrib import admin
from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modified_dt',)
    list_filter = ('modified_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
