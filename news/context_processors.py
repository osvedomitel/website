from news.models import Category, Issue


def navigation(request):
    """
    Return context variables provided by the news app for site-wide use.
    """
    return {
        'categories': Category.objects.all(),
        'current_issue': Issue.objects.filter(online=True).latest()
    }
