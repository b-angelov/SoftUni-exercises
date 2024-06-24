# Generated by Django 5.0.4 on 2024-06-22 15:41

from django.db import migrations

def create_unique_brands(apps,schema_editor):
    shoes = apps.get_model("main_app","Shoe")
    brands = apps.get_model("main_app", "UniqueBrands")

    db_alias = schema_editor.connection.alias

    unique_brand_names = shoes.objects.values_list("brand",flat=True).distinct()

    for brand in unique_brand_names:
        brands.objects.using(db_alias).create(brand_name=brand)

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands)
    ]
