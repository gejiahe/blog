from django.contrib import admin
from .models import *
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','index','name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','index','name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'click_count',)

    # 3.引入媒体文件
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'pk','content', 'user', 'article',)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links)
