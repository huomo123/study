from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    isdel = models.IntegerField()
    password = models.CharField(max_length=20)
    create_time = models.CharField(max_length=20)
    update_time = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'user'

