# Generated by Django 3.2.4 on 2021-08-24 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_article_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like',
        ),
    ]