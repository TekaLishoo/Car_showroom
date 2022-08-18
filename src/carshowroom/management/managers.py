from django.db import models


class CarShowRoomManager(models.Manager):
    def save(self, *args, **kwargs):
        print(kwargs['title'])
        if 'title' in kwargs and isinstance(kwargs['title'], str):
            # kwargs['type'] = HardwareType.objects.get(name=kwargs['type'])
            kwargs['title'] = f'{kwargs["title"]} the best'
            super(CarShowRoomManager, self).save(*args, **kwargs)
