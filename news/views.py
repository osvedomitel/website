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
    return render(request, 'all_issues.html', {'issues': issues})


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
    context = {
        'category': category,
        'articles': category.article_set.all()
    }
    return render(request, 'category.html', context)


def keyword(request, slug):
    keyword = get_object_or_404(Keyword, slug=slug)
    context = {
        'keyword': keyword,
        'articles': keyword.article_set.all()
    }
    return render(request, 'keyword.html', context)
