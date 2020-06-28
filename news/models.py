from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


"""
authors
"""


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='потребител'
    )
    slug = models.SlugField(allow_unicode=True, verbose_name='охлюв')
    bio = models.TextField(blank=True, verbose_name='животоописание')

    created = models.DateTimeField(auto_now_add=True, verbose_name='създаден')
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='последна промяна'
    )

    class Meta:
        verbose_name = 'авторски профил'
        verbose_name_plural = 'авторски профили'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('author', args=[self.slug])


"""
taxonomy
"""


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='име')
    slug = models.SlugField(
        allow_unicode=True, unique=True, verbose_name='охлюв'
    )
    order = models.PositiveSmallIntegerField(verbose_name='пореден номер')

    created = models.DateTimeField(auto_now_add=True, verbose_name='създадена')
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='последна промяна'
    )

    class Meta:
        ordering = ('order',)
        verbose_name = 'рубрика'
        verbose_name_plural = 'рубрики'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])


class Keyword(models.Model):
    keyword = models.CharField(max_length=50, verbose_name='ключова дума')
    slug = models.SlugField(
        allow_unicode=True, unique=True, verbose_name='охлюв'
    )
    order = models.PositiveSmallIntegerField(verbose_name='пореден номер')

    created = models.DateTimeField(auto_now_add=True, verbose_name='създадена')
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='последна промяна'
    )

    class Meta:
        ordering = ('order',)
        verbose_name = 'ключова дума'
        verbose_name_plural = 'ключови думи'

    def __str__(self):
        return self.keyword

    def get_absolute_url(self):
        return reverse('keyword', args=[self.slug])


"""
issues
"""


class IssueQuerySet(models.QuerySet):

    def with_blocks(self):
        return self.prefetch_related(models.Prefetch(
            'article_set',
            Article.objects.filter(block__gte=0).order_by('block'),
            to_attr='blocks'
        ))


class Issue(models.Model):
    published = models.DateField(
        default=date.today, verbose_name='дата на издаване'
    )
    number = models.PositiveSmallIntegerField(
        unique_for_year='published', verbose_name='номер на броя'
    )
    online = models.BooleanField(verbose_name='онлайн')

    created = models.DateTimeField(auto_now_add=True, verbose_name='създаден')
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='последна промяна'
    )

    objects = IssueQuerySet.as_manager()

    class Meta:
        get_latest_by = 'published'
        verbose_name = 'брой'
        verbose_name_plural = 'броеве'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        year, month = self.published.year, self.published.month
        return reverse('issue', args=[year, month])

    @property
    def volume(self):
        return self.published.year - 2018

    @property
    def name(self):
        return 'Брой {}, година {}'.format(self.number, self.volume)


"""
articles
"""


class Article(models.Model):
    BLOCK_CHOICES = (
        (-1, '− (не е на първа страница)'),
        (0, 'горе вляво'),
        (1, 'горе по средата и вдясно'),
        (2, 'долу вляво'),
        (3, 'горното средно'),
        (4, 'долното средно'),
        (5, 'долу вдясно'),
        (6, 'най-долу по средата'),
    )

    title = models.CharField(max_length=200, verbose_name='заглавие')
    slug = models.SlugField(allow_unicode=True, verbose_name='охлюв')

    subtitle = models.CharField(
        max_length=200, blank=True, verbose_name='подзаглавие'
    )
    text = models.TextField(verbose_name='текст')
    truncate_after = models.PositiveSmallIntegerField(
        default=100, verbose_name='отрязване след дума'
    )

    issue = models.ForeignKey(
        Issue, on_delete=models.PROTECT, verbose_name='брой'
    )
    order = models.PositiveSmallIntegerField(verbose_name='пореден номер')
    block = models.SmallIntegerField(
        choices=BLOCK_CHOICES, default=-1, verbose_name='блокче'
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='рубрика'
    )
    keywords = models.ManyToManyField(
        Keyword, blank=True, verbose_name='ключови думи'
    )
    authors = models.ManyToManyField(User, blank=True, verbose_name='автори')

    is_extra = models.BooleanField(
        default=False, verbose_name='притурена',
        help_text=(
            'Ако една статия е отбелязана като притурена към броя си, '
            'тогава датата ѝ на издаване е датата ѝ на създаване '
            'вместо датата на издаване на броя ѝ.'
        )
    )

    social_image = models.ImageField(
        null=True, blank=True, upload_to='articles/social',
        verbose_name='картинка при споделяне'
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name='създадена')
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='последна промяна'
    )

    class Meta:
        unique_together = ('issue', 'slug')
        ordering = ('order',)
        verbose_name = 'статия'
        verbose_name_plural = 'статии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        year, month = self.issue.published.year, self.issue.published.month
        return reverse('article', args=[year, month, self.slug])

    @property
    def author_names(self):
        return [
            author.get_full_name()
            for author in self.authors.order_by('first_name')
        ]

    @property
    def published(self):
        return self.created if self.is_extra else self.issue.published
