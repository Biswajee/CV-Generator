from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    name = models.CharField(max_length=15)


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    univ = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    ph = models.CharField(max_length=50)
    cph = models.CharField(max_length=50)
    cemail = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=50)
    skill_1 = models.CharField(max_length=50)
    skill_2 = models.CharField(max_length=50)
    skill_3 = models.CharField(max_length=50)
    skill_4 = models.CharField(max_length=50)
    skill_5 = models.CharField(max_length=50)
    skill_6 = models.CharField(max_length=50)
    xp_1_title = models.CharField(max_length=50)
    xp_2_title = models.CharField(max_length=50)
    xp_3_title = models.CharField(max_length=50)
    xp_4_title = models.CharField(max_length=50)
    xp_5_title = models.CharField(max_length=50)
    xp_6_title = models.CharField(max_length=50)
    xp_1_desc = models.CharField(max_length=50)
    xp_2_desc = models.CharField(max_length=50)
    xp_3_desc = models.CharField(max_length=50)
    xp_4_desc = models.CharField(max_length=50)
    xp_5_desc = models.CharField(max_length=50)
    xp_6_desc = models.CharField(max_length=50)

    def __str__(self):
        data = {
            "General information": {
                "name": self.name,
                "position": self.position,
                "university": self.univ,
                "email": self.email,
                "session": self.session,
                "phone": self.ph,
                "college contact": self.cph,
                "college email": self.cemail,
                "self description": self.desc,
            },
            "Academic Qualification": {"cgpa": self.cgpa},
            "Skills": {
                "Skill 1": self.skill_1,
                "Skill 2": self.skill_2,
                "Skill 3": self.skill_3,
                "Skill 4": self.skill_4,
                "Skill 5": self.skill_5,
                "Skill 6": self.skill_6,
            },
            "Experience": {
                "Experience 1": self.xp_1_title,
                "Description 1": self.xp_1_desc,
                "Experience 2": self.xp_2_title,
                "Description 2": self.xp_2_desc,
                "Experience 3": self.xp_3_title,
                "Description 3": self.xp_3_desc,
                "Experience 4": self.xp_4_title,
                "Description 4": self.xp_4_desc,
                "Experience 5": self.xp_5_title,
                "Description 5": self.xp_5_desc,
                "Experience 6": self.xp_6_title,
                "Description 6": self.xp_6_desc,
            },
        }