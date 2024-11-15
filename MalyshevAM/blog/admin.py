from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)   

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return 'Нет фото'
    get_photo.short_description = 'Фото'

    save_as = True
    save_on_top = True

    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)

    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}   

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}