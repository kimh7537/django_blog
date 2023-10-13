from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}   #name필드를 활용해 slug를 자동으로 채워줌

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
