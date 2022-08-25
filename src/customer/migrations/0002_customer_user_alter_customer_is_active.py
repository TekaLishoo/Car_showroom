# Generated by Django 4.0.7 on 2022-08-23 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
