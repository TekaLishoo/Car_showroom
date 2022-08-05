# Generated by Django 4.1 on 2022-08-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carshowroom", "0004_alter_carshowroom_wishes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carshowroom",
            name="wishes",
            field=models.JSONField(
                default='{"body_type": "Sedan", "engine_size": 1.0, "drive_type": "Rear"}'
            ),
        ),
    ]