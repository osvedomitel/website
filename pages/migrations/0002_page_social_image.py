# Generated by Django 3.1.2 on 2021-03-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='social_image',
            field=models.ImageField(blank=True, null=True, upload_to='pages/social', verbose_name='картинка при споделяне'),
        ),
    ]
