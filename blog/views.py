from django.shortcuts import render, redirect, get_object_or_404
from blog.models import *
from django.db.models import Q
from django.db.models import Count, F, Value
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from blog.forms import *
# Create your views here.


def index(request):
    return redirect("home")


def home(request):
    first_category = Category.objects.all()[0]
    context = {
        'last_posts' : Post.objects.all().order_by('-created')[:5],
        'categories' : Category.objects.all(),
        'first_category_url' : "{% url 'by_category'  '" + first_category.slug + "' %}",
        }
    
    return render(request, template_name='blog/home.html', context=context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    related_posts = Post.objects.filter(Q(category=post.category) | Q(title__icontains=post.category) | Q(content__icontains=post.category)).exclude(slug=post.slug)
    
    post.views += 1
    post.save()
    
    comments = Comment.objects.filter(post=post)
    comments_count = comments.count()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    
    context = {
        'post' : post,
        'related_posts': related_posts,
        'comments': comments,
        'comments_count': comments_count,
        'comment_form': comment_form
    }
    
    return render(request, template_name='blog/post.html', context=context)


def by_category(request, slug):
    category = Category.objects.get(slug=slug)
    posts_by_category = Post.objects.filter(category__slug=category.slug)
    categories = Category.objects.all()
    context = {
        'category' : category,
        'posts_by_category' : posts_by_category,
        'categories': categories
    }
    
    return render(request, 'blog/by_category.html',context=context)



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUser()
    
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'form': form}
    return render(request, 'registration/register.html', context=context)
        
        
def all_posts(request):
    posts = Post.objects.all().order_by('-created')
    categories = Category.objects.all()
    
    context = {
        'posts_by_category': posts,
        'categories': categories,
    }
    
    return render(request, 'blog/all_posts.html', context=context)