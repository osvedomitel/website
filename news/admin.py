from django.contrib import admin

from news.models import Article, Category, Issue, Keyword


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'last_modified',)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'order',)
        }),
        ('Хронология', {
            'classes': ('collapse',),
            'fields': ('created', 'last_modified',)
        })
    )
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created', 'last_modified',)


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'order', 'last_modified',)
    search_fields = ('keyword',)
    fieldsets = (
        (None, {
            'fields': ('keyword', 'slug', 'order',)
        }),
        ('Хронология', {
            'classes': ('collapse',),
            'fields': ('created', 'last_modified',)
        })
    )
    prepopulated_fields = {'slug': ('keyword',)}
    readonly_fields = ('created', 'last_modified',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'published', 'online', 'last_modified',)
    ordering = ('-published',)
    fieldsets = (
        (None, {
            'fields': ('published', 'number', 'online',)
        }),
        ('Хронология', {
            'classes': ('collapse',),
            'fields': ('created', 'last_modified',)
        })
    )
    readonly_fields = ('created', 'last_modified',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue', 'category', 'last_modified',)
    ordering = ('-issue__published', 'order',)
    list_filter = ('category', 'issue',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'subtitle', 'text', 'truncate_after',)
        }),
        ('Таксономия', {
            'fields': (
                'issue', 'order', 'block', 'category', 'keywords', 'authors',
                'is_extra',
            )
        }),
        ('Хронология', {
            'classes': ('collapse',),
            'fields': ('created', 'last_modified',)
        })
    )
    autocomplete_fields = ('keywords', 'authors',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'last_modified',)
