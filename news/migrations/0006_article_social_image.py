# Generated by Django 3.0.3 on 2020-06-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_is_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='social_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/social', verbose_name='картинка при споделяне'),
        ),
    ]
