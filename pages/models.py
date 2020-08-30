from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='заглавие')
    slug = models.SlugField(
        allow_unicode=True, unique=True, verbose_name='охлюв'
    )

    text = models.TextField(verbose_name='текст')

    created = models.DateTimeField(auto_now_add=True, verbose_name='създадена')
    last_modified = models.DateTimeField(
        auto_now=True, verbose_name='последна промяна'
    )

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страници'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[self.slug])
