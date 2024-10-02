# Generated by Django 5.1.1 on 2024-10-01 18:34

import TastyRecipes.recipes.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Nickname must be at least 2 chars long!')])),
                ('first_name', models.CharField(max_length=30, validators=[TastyRecipes.recipes.validators.FirstCapital()])),
                ('last_name', models.CharField(max_length=30, validators=[TastyRecipes.recipes.validators.FirstCapital()])),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': '"We already have a recipe with the same title!"'}, max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('cuisine_type', models.CharField(choices=[('FR', 'French'), ('CH', 'Chinese'), ('IT', 'Italian'), ('BK', 'Balkan'), ('OT', 'Other')], max_length=7)),
                ('ingredients', models.TextField(help_text='Ingredients must be separated by a comma and space.')),
                ('instructions', models.TextField()),
                ('cooking_time', models.PositiveIntegerField(help_text='Provide the cooking time in minutes.', validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='recipes.profile')),
            ],
        ),
    ]
