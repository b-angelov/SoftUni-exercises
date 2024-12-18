# Generated by Django 5.1.1 on 2024-10-06 17:15

import django.core.validators
import django.db.models.deletion
import world_of_speed.accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_delete_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('RY', 'Rally'), ('OW', 'Open-wheel'), ('KT', 'Kart'), ('DG', 'Drag'), ('OT', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinValueValidator(1)])),
                ('year', models.IntegerField(validators=[world_of_speed.accounts.validators.ValueInRange(1999, 2030)])),
                ('image_url', models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, help_text='https://...', unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
