from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
class PostListView(ListView):
	model = Post
	template_name = 'blog/list.html'
	context_object_name = 'posts'
class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail.html'
	context_object_name = 'post'