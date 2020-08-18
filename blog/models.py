from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=128, blank=False, verbose_name="Category Title")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("by_category", kwargs={"slug": self.slug})
    


class Post(models.Model):
    title = models.CharField(max_length=128, blank=False, verbose_name="Post Title")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_posts")
    content = models.TextField(verbose_name="Post Content", blank=False)
    photo = models.ImageField(upload_to="assets/photos/%Y/%m/%d", blank=True, verbose_name="Post Image")
    attached_file = models.FileField(upload_to='assets/files/%Y/%m', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts_by_category', null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
        

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments', blank=True)
    
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_comments")
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['created']