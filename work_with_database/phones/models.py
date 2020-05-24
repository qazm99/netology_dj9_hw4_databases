from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    #, , , ,  и
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    lte_exists = models.BooleanField()
    release_date = models.DateField()
    slug = models.CharField(max_length=255)
    pass

    def __str__(self):
        return f'id:{self.id}, name:{self.name}, price:{self.price}'
