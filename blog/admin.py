from django.contrib import admin
from blog.models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'created', 'views', 'category')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')
    readonly_fields = ('created', 'views')
    
    save_as = True
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created', 'active',)
    list_display_links = ('author',)
    list_editable = ('active',)    
    
    readonly_fields = ('created',)
