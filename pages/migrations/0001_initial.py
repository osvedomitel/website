# Generated by Django 3.0.7 on 2020-08-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заглавие')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='охлюв')),
                ('text', models.TextField(verbose_name='текст')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='създадена')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='последна промяна')),
            ],
            options={
                'verbose_name': 'страница',
                'verbose_name_plural': 'страници',
            },
        ),
    ]