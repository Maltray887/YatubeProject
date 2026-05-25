from django.contrib import admin
<<<<<<< HEAD
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', )
    search_fields = ('text', )
    list_filter = ('pub_date', )
    list_editable = ('group', )
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description',)
    search_fields = ('title',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)



=======

# Register your models here.
>>>>>>> be3674557d6818f3f9386a83a7f90ff13d410aaa
