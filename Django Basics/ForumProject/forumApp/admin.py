from django.contrib import admin

from forumApp.models import Author, Post, Articles, URLs


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    pass

@admin.register(URLs)
class URLsAdmin(admin.ModelAdmin):
    pass

