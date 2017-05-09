from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Post
from .forms import PostForm
from .models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render_to_response('index.html', {'posts': posts})


def post(request, id):
    current_post = get_object_or_404(Post, pk=id)
    return render_to_response('post.html', {'post': current_post})


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(is_active=True)


class PostAutorListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        self.author_id = author_id
        return super().get(request, *args, **kwargs)


    def get_queryset(self):
        posts = Post.objects.filter(user__id=self.author_id)
        if self.request.user.is_superuser:
            return posts
        else:
            return posts.filter(is_active=True)



class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    success_url = '/'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    success_url = '/'
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_confirm.html'
    success_url = '/'
    context_object_name = 'post'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
