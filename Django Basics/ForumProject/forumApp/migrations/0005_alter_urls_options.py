# Generated by Django 5.1.1 on 2024-09-20 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumApp', '0004_alter_articles_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name': 'URL', 'verbose_name_plural': 'URLs'},
        ),
    ]
