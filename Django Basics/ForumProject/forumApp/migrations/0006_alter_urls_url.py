# Generated by Django 5.1.1 on 2024-09-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumApp', '0005_alter_urls_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.TextField(blank=True, default=''),
        ),
    ]