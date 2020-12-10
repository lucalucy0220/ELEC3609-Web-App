from django.contrib import admin
from recipe.models import Profile, Post

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'firstname','lastname','dob', 'picture']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'timestamp','short_content','post_img', 'category'] #add a category field?
    search_fields = ['id', 'user__username', 'title', 'content']   # To search through posts in admin list


# Register/importing the two models: Profile and Post
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Post, PostAdmin)
