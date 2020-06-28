from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from news.models import Article, Category, Issue, Keyword


def home(request):
    issue = Issue.objects.with_blocks().filter(online=True).latest()
    return render(request, 'home.html', {'issue': issue})


def issue(request, year, month):
    issue = get_object_or_404(
        Issue,
        online=True,
        published__year=year,
        published__month=month
    )
    context = {
        'issue': issue,
        'articles': issue.article_set.order_by('order')
    }
    return render(request, 'issue.html', context)


def all_issues(request):
    issues = Issue.objects.filter(online=True).order_by('-published')
    context = {
        'issues': issues,
        'active_nav_item': 'all_issues'
    }
    return render(request, 'all_issues.html', context)


def article(request, year, month, slug):
    article = get_object_or_404(
        Article.objects.select_related('issue'),
        issue__published__year=year,
        issue__published__month=month,
        slug=slug
    )
    return render(request, 'article.html', {'article': article})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    articles = category.article_set \
                    .filter(issue__online=True) \
                    .order_by('-issue__published', 'order')

    context = {
        'category': category,
        'articles': articles,
        'active_nav_item': category.slug
    }
    return render(request, 'category.html', context)


def keyword(request, slug):
    keyword = get_object_or_404(Keyword, slug=slug)

    articles = keyword.article_set \
                    .filter(issue__online=True) \
                    .order_by('-issue__published', 'order')

    context = {
        'keyword': keyword,
        'articles': articles
    }
    return render(request, 'keyword.html', context)


def author(request, slug):
    author = get_object_or_404(User, profile__slug=slug)

    articles = author.article_set \
                    .filter(issue__online=True) \
                    .order_by('-issue__published', 'order',)

    context = {
        'author': author,
        'articles': articles
    }
    return render(request, 'author.html', context)
