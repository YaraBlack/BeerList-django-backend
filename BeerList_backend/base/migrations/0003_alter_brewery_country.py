# Generated by Django 5.1.5 on 2025-01-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_brewery_rename_ingridients_beer_ingredients_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brewery",
            name="country",
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
