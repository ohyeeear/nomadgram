from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_displat_links = (
        'location',
        'caption',
    )

    search_fields = (

        'location',
        'caption',
    )

    list_display = (
    'created_at',
    'updated_at',
    'file', 
    'location',
    'caption',
    'creator',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
   
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )