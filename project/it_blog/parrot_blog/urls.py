"""parrot_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from about_app.views import about
from main_app.views import PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView, PostAutorListView
from user_app.views import logout, login, registration
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name='index'),
    url(r'^(?P<author_id>\d+)/$', PostAutorListView.as_view(), name='by_author'),
    url(r'^about/$', about, name='about'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
    url(r'^post/add/$', login_required(PostCreateView.as_view()), name='add_post'),
    url(r'^post/edit/(?P<pk>\d+)/$', login_required(PostUpdateView.as_view()), name='edit_post'),
    url(r'^post/delete/(?P<pk>\d+)/$', login_required(PostDeleteView.as_view()), name='delete_post'),
    url(r'user/login/', login, name='login'),
    url(r'user/logout/', logout, name='logout'),
    url(r'user/registration/', registration, name='registration'),
]
