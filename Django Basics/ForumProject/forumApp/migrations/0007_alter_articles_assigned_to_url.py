# Generated by Django 5.1.1 on 2024-09-20 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumApp', '0006_alter_urls_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='assigned_to_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='forumApp.urls'),
        ),
    ]
