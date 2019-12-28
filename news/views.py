from django.shortcuts import get_object_or_404, render

from news.models import Article, Category, Issue, Keyword


def home(request):
    issue = Issue.objects.with_blocks().filter(online=True).latest()
    return render(request, 'home.html', {'issue': issue})


def issue(request, year, month):
    issue = get_object_or_404(
        Issue.objects.with_blocks(),
        online=True,
        published__year=year,
        published__month=month
    )
    return render(request, 'issue.html', {'issue': issue})


def all_issues(request):
    issues = Issue.objects.filter(online=True)
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
    return render(request, 'category.html', {'category': category})


def keyword(request, slug):
    keyword = get_object_or_404(Keyword, slug=slug)
    return render(request, 'keyword.html', {'keyword': keyword})
