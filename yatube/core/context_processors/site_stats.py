from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

def site_stats(request):
    return {
        'site_stats': {
            'posts_count': Post.objects.count(),
            'authors_count': User.objects.filter(posts__isnull=False).distinct().count()
        }
    }