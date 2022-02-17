from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post 


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'post_new.html'
    model = Post
    fields = ["title", "author", "body"]

class PostUpdateView(UpdateView):
    template_name = 'post_edit.html'
    model = Post
    fields =  ["title", "body"]

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('home')

# Create your views here.
