# Generated by Django 3.0.7 on 2020-06-28 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_article_social_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(verbose_name='животоописание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='създаден')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='последна промяна')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='потребител')),
            ],
            options={
                'verbose_name': 'авторски профил',
                'verbose_name_plural': 'авторски профили',
            },
        ),
    ]
