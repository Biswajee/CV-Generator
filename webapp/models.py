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

class resume_data():
    # usr_id must be foreign key for reg_info table's usr_id.
    usr_id = models.IntegerField(null=False, primary_key=True, unique=True)

    name = models.TextField(null=False)
    position = models.TextField(null=False)
    univ = models.TextField(null=False)
    email = models.TextField(null=False, unique=True)
    session = models.TextField(null=False)
    ph = models.TextField(null=False)
    cph = models.TextField(null=False)
    cemail = models.TextField(null=False)
    desc = models.TextField(null=False)
    cgpa = models.TextField(null=False, unique=True)
    skill_1 = models.TextField()
    skill_2 = models.TextField()
    skill_3 = models.TextField()
    skill_4 = models.TextField()
    skill_5 = models.TextField()
    skill_6 = models.TextField()
    xp_1_title = models.TextField()
    xp_2_title = models.TextField()
    xp_3_title = models.TextField()
    xp_4_title = models.TextField()
    xp_5_title = models.TextField()
    xp_6_title = models.TextField()
    
