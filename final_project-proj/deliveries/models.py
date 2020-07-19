from django.db import models
from django.contrib.auth.models import User
from enum import  Enum, EnumMeta

# Create your models here.

class deliveries(models.Model):
    GUSH_DAN = 'GD'
    RAMAT_HAGOLAN = 'RH'
    HASHFELA = 'HS'
    DAROM = 'DR'
    GALIL = 'GL'
    AREA_CHOISES = [
        (GUSH_DAN, 'Gush Dan'),
        (RAMAT_HAGOLAN, 'Ramat Hagolan'),
        (HASHFELA, 'Hashfela'),
        (DAROM, 'Darom'),
        (GALIL, 'Galil'),
    ]
    area = models.CharField(
        max_length=2,
        choices=AREA_CHOISES,
        default=GUSH_DAN,
    )

    MAIL='MA'
    FOOD= 'FO'
    FLOWERS='FL'
    GIFT='GF'
    MYSTERYBOX='MB'
    TYPE_CHOICES = [
        (MAIL,'Mail'),
        (FOOD,'Food'),
        (FLOWERS,'Flowers'),
        (GIFT,'Gift'),
        (MYSTERYBOX,'Mystery Box')
    ]
    delType = models.CharField(
        max_length=11,
        choices=TYPE_CHOICES,
        default=MAIL
    )
    class Status(models.IntegerChoices):
        i_will_take_it=0
        im_on_my_way = 1
        delivery_has_arrieved = 2
        finish_delivery=3
    status = models.IntegerField(choices=Status.choices, default=0)
    class Size(models.IntegerChoices):
        S=0
        M = 1
        L = 2
    size = models.IntegerField(choices=Size.choices, default=0)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    deliveryman = models.ForeignKey( User,blank=True, null=True,on_delete=models.SET_NULL,related_name='+')
    description = models.CharField(max_length=256,blank=True,null=True)
    title = models.CharField(max_length=80)

