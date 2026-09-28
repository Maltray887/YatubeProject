from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Group

import datetime

ALLOWED_PER_PAGE = (1,10,25)

def index(request):
    post_list = Post.objects.all().order_by('pub_date')
    total_posts = post_list.count()

    per_page_row =  request.GET.get('per_page', 10)
    is_all = per_page_row == "all"

    if is_all:
        per_page = min(total_posts, 1000) or 1
    else:
        try:
            per_page = int(per_page_row)
            if per_page not in ALLOWED_PER_PAGE:
                per_page = 10
        except(ValueError, TypeError):
            per_page = 10 

    paginator = Paginator(post_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 
        'per_page': 'all' if is_all else per_page,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts
    }

    return render(request, 'posts/group_list.html', context)

def morning_post_view(request):
    start_date = datetime.datetime(1854,7,7)
    end_date = datetime.datetime(1854,7,21)
    
    posts = Post.objects.filter(
        text__icontains='Утром',
        author__username='leo',
        pub_date__range=(start_date, end_date),
        )
    
    return render(request, 'posts/index.html', {'posts':posts})
    