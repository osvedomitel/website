from django.contrib import admin

from news.models import Article, Category, Issue, Keyword


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'last_modified',)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'weight',)
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
    list_display = ('keyword', 'last_modified',)
    fieldsets = (
        (None, {
            'fields': ('keyword', 'slug',)
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
    list_filter = ('category', 'issue',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'subtitle', 'text',)
        }),
        ('Таксономия', {
            'fields': ('issue', 'block', 'category', 'keywords',)
        }),
        ('Хронология', {
            'classes': ('collapse',),
            'fields': ('created', 'last_modified',)
        })
    )
    filter_horizontal = ('keywords',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'last_modified',)
