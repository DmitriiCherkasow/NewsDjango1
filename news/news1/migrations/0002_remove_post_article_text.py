# Generated by Django 4.1.4 on 2022-12-19 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='article_text',
        ),
    ]
