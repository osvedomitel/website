from django.contrib import admin

from news.models import Article, Category, Issue, Keyword


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    pass


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
