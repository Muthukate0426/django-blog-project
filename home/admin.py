from django.contrib import admin

from .models import Contact, Profile, Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'created_at'
    )

    search_fields = (
        'title',
        'content'
    )

    list_filter = (
        'created_at',
        'author'
    )





@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'created_at'
    )

    search_fields = (
        'name',
        'email'
    )






@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
    )