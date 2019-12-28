from news.models import Category


def navigation(request):
    """
    Return context variables provided by the news app for site-wide use.
    """
    return {
        'categories': Category.objects.all()
    }
