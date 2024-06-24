# Generated by Django 5.0.4 on 2024-06-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('main_app', '0001_initial'), ('main_app', '0003_uniquebrands')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('size', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UniqueBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
