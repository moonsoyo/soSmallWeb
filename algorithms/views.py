from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'algorithms/index.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post