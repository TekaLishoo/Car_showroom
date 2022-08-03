from django.db import models


class CommonPart(models.Model):
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
