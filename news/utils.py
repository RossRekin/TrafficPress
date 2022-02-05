from .models import Category, Article


def filter_articles_by_category(request):
    category_query = None

    if request.GET.get('category'):
        category_query = request.GET.get('category')
        category = Category.objects.all().filter(name=category_query)
        articles = Article.objects.all().filter(categories__in=category)
    else:
        articles = Article.objects.all()

    return articles, category_query
