from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,  # views.py 에서 데이터베이스에 쿼리를 날려서 원하는 레코드를 가져올 수 있음.
        }
    )
