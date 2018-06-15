from django.db import models
import random
# Create your models here.


def generateId():
    return random.randint(1,50)*3

class reg_info(models.Model):
    usr_id = models.IntegerField(null=False, default=generateId(), primary_key=True, unique=True)
    email = models.TextField(null=False, unique=True)
    password = models.TextField(null=False)
    date = models.DateTimeField()

    def __str__(self):
        return (self.usr_id+'\n'+self.date+'\n'+self.email+'\n'+self.password)
