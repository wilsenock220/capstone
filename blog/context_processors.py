from .models import Article

def articles_count(request):
    count = Article.objects.count()
    return {'articles_count': count}
    