from django.db import models
import random
from datetime import date

from flask import jsonify
# Create your models here.


def generateId():
    return random.randint(1,50)*3

class reg_info(models.Model):
    usr_id = models.IntegerField(default=generateId(), primary_key=True, unique=True)
    email = models.TextField(unique=True)
    password = models.TextField(default="admin")
    phone = models.IntegerField(default=8888)
    name = models.TextField(default="noname")
    date = models.DateTimeField(date.today())

    def __str__(self):

    #    api_data = {
    #                'credentials': {
    #                        'user_id': self.usr_id,
    #                        'registration date': self.date,
    #                        'registered email': self.email,
    #                        'name': self.name,
    #                        'phone': self.phone
    #                        }
    #                }
    #    return jsonify(api_data)

        return (self.usr_id+'\n'+self.date+'\n'+self.email+'\n'+self.password+'\n'+self.name+'\n'+self.phone)



class resume_data(models.Model):
    # usr_id must be foreign key for reg_info table's usr_id.
    usr_id = models.ForeignKey(reg_info, on_delete=models.CASCADE)

    name = models.TextField()
    position = models.TextField()
    univ = models.TextField()
    email = models.TextField(unique=True)
    session = models.TextField()
    ph = models.TextField()
    cph = models.TextField()
    cemail = models.TextField()
    desc = models.TextField()
    cgpa = models.TextField()
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
    xp_1_desc = models.TextField()
    xp_2_desc = models.TextField()
    xp_3_desc = models.TextField()
    xp_4_desc = models.TextField()
    xp_5_desc = models.TextField()
    xp_6_desc = models.TextField()
    xp_1_session = models.DateField()
    xp_2_session = models.DateField()
    xp_3_session = models.DateField()
    xp_4_session = models.DateField()
    xp_5_session = models.DateField()
    xp_6_session = models.DateField()


    def __str__(self):

    #    return (self.name+'\n'+self.position+'\n'+self.univ+'\n'+self.email+'\n'+self.session+'\n'+self.ph+'\n'+self.cph+'\n'+self.cemail+'\n'+self.desc+'\n'+self.cgpa
    #            +'\n'+self.skill_1+'\n'+self.skill_2+'\n'+self.skill_3+'\n'+self.skill_4+'\n'+self.skill_5+'\n'+self.skill_6+'\n'+self.xp_1_title+'\n'+self.xp_2_title+'\n'+self.xp_3_title
    #            +'\n'+self.xp_4_title+'\n'+self.xp_5_title+'\n'+self.xp_6_title+'\n'+self.xp_1_desc+'\n'+self.xp_2_desc+'\n'+self.xp_3_desc+'\n'+self.xp_4_desc+'\n'+self.xp_5_desc+'\n'+self.xp_6_desc)
    #            +'\n'+self.xp_1_session+'\n'+self.xp_2_session+'\n'+self.xp_3_session+'\n'+self.xp_4_session+'\n'+self.xp_5_session+'\n'+self.xp_6_session)
        data = {
                'General information': {
                            'name': self.name,
                            'position': self.position,
                            'university': self.univ,
                            'email': self.email,
                            'session': self.session,
                            'phone': self.ph,
                            'college contact': self.cph,
                            'college email': self.cemail,
                            'self description': self.desc,
                    },
                'Academic Qualification': {
                            'cgpa': self.cgpa
                    }

                }
        return jsonify(data)
