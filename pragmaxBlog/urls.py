"""pragmaxBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pragmaxBlog import settings
from django.conf.urls.static import static
import blog.views as blog_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index),
    path('home/', blog_views.home, name="home"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', blog_views.register, name="register"),
    path('post/<str:slug>', blog_views.single_post, name='post_detail'),
    path('category/<str:slug>', blog_views.by_category, name="by_category"),
    path('tag/<str:slug>', blog_views.by_tag, name="by_tag"),
    path('all_posts/', blog_views.all_posts, name="all_posts")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
