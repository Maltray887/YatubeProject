from django.shortcuts import render, get_object_or_404

from .models import Post, Group

import datetime

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'posts': posts}
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
    