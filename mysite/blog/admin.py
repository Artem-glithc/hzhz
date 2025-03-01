from django.contrib import admin

# Register your models here.
from .models import Post, PostPoint

# admin.site.register(Post)
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


admin.site.register(PostPoint)