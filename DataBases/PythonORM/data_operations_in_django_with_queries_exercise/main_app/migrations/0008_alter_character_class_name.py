# Generated by Django 5.0.4 on 2024-06-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='class_name',
            field=models.CharField(choices=[('M', 'Mage'), ('W', 'Warrior'), ('A', 'Assassin'), ('S', 'Scout')], max_length=20),
        ),
    ]
