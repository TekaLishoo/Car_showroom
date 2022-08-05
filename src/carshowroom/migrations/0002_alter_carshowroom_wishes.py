# Generated by Django 4.1 on 2022-08-04 19:23

from django.db import migrations, models
import src.core.wishes


class Migration(migrations.Migration):

    dependencies = [
        ("carshowroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carshowroom",
            name="wishes",
            field=models.JSONField(default=src.core.wishes.default_showroom_wishes),
        ),
    ]