# Generated by Django 3.0.1 on 2020-01-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_truncate_after'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='охлюв'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='охлюв'),
        ),
    ]
