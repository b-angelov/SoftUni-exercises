# Generated by Django 5.0.4 on 2024-06-22 18:44

from django.db import migrations

def set_price(apps,schema_editor):
    Smartphone = apps.get_model("main_app","Smartphone")
    for smartphone in Smartphone.objects.all():
        smartphone.price = len(smartphone.brand) * 120
        smartphone.save()

def set_category(apps,schema_editor):
    Smartphone = apps.get_model("main_app","Smartphone")
    for smartphone in Smartphone.objects.all():
        if smartphone.price >= 750:
            smartphone.category = "Expensive"
        else:
            smartphone.category = "Cheap"
        smartphone.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_price),
        migrations.RunPython(set_category)
    ]