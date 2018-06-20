from django.shortcuts import render
from webapp.models import resume_data, generateId, reg_info
from django.http import HttpResponse
from flask import jsonify
import json
# Create your views here.


def json_endpoint(request):
    for i in range(1,2):
        name = resume_data.objects.values_list('name', flat=True).get(id=i)
        position = resume_data.objects.values_list('position', flat=True).get(id=i)
        univ = resume_data.objects.values_list('univ', flat=True).get(id=i)
        email = resume_data.objects.values_list('email', flat=True).get(id=i)
        session = resume_data.objects.values_list('session', flat=True).get(id=i)
        ph = resume_data.objects.values_list('ph', flat=True).get(id=i)
        cemail = resume_data.objects.values_list('cemail', flat=True).get(id=i)
        cph = resume_data.objects.values_list('cph', flat=True).get(id=i)
        desc = resume_data.objects.values_list('desc', flat=True).get(id=i)
        cgpa = resume_data.objects.values_list('cgpa', flat=True).get(id=i)
        skill_1 = resume_data.objects.values_list('skill_1', flat=True).get(id=i)
        skill_2 = resume_data.objects.values_list('skill_2', flat=True).get(id=i)
        skill_3 = resume_data.objects.values_list('skill_3', flat=True).get(id=i)
        skill_4 = resume_data.objects.values_list('skill_4', flat=True).get(id=i)
        skill_5 = resume_data.objects.values_list('skill_5', flat=True).get(id=i)
        skill_6 = resume_data.objects.values_list('skill_6', flat=True).get(id=i)
        xp_1_title = resume_data.objects.values_list('xp_1_title', flat=True).get(id=i)
        xp_2_title = resume_data.objects.values_list('xp_2_title', flat=True).get(id=i)
        xp_3_title = resume_data.objects.values_list('xp_3_title', flat=True).get(id=i)
        xp_4_title = resume_data.objects.values_list('xp_4_title', flat=True).get(id=i)
        xp_5_title = resume_data.objects.values_list('xp_5_title', flat=True).get(id=i)
        xp_6_title = resume_data.objects.values_list('xp_6_title', flat=True).get(id=i)
        xp_1_session = resume_data.objects.values_list('xp_1_session', flat=True).get(id=i)
        xp_2_session = resume_data.objects.values_list('xp_2_session', flat=True).get(id=i)
        xp_3_session = resume_data.objects.values_list('xp_3_session', flat=True).get(id=i)
        xp_4_session = resume_data.objects.values_list('xp_4_session', flat=True).get(id=i)
        xp_5_session = resume_data.objects.values_list('xp_5_session', flat=True).get(id=i)
        xp_6_session = resume_data.objects.values_list('xp_6_session', flat=True).get(id=i)
        xp_1_desc = resume_data.objects.values_list('xp_1_desc', flat=True).get(id=i)
        xp_2_desc = resume_data.objects.values_list('xp_2_desc', flat=True).get(id=i)
        xp_3_desc = resume_data.objects.values_list('xp_3_desc', flat=True).get(id=i)
        xp_4_desc = resume_data.objects.values_list('xp_4_desc', flat=True).get(id=i)
        xp_5_desc = resume_data.objects.values_list('xp_5_desc', flat=True).get(id=i)
        xp_6_desc = resume_data.objects.values_list('xp_6_desc', flat=True).get(id=i)
        user_id = resume_data.objects.values_list('usr_id', flat=True).get(id=i)


        context = {i :[{
        'name':name,
        'position':position,
        'univ': univ,
        'session': session,
        'email': email,
        'ph': ph,
        'cph': cph,
        'cemail': cemail,
        'desc': desc,
        'cgpa': cgpa,
        'skill_1': skill_1,
        'skill_2': skill_2,
        'skill_3': skill_3,
        'skill_4': skill_4,
        'skill_5': skill_5,
        'skill_6': skill_6,
        'xp_1_title': xp_1_title,
        'xp_2_title': xp_2_title,
        'xp_3_title': xp_3_title,
        'xp_4_title': xp_4_title,
        'xp_5_title': xp_5_title,
        'xp_6_title': xp_6_title,
        'xp_1_session': xp_1_session,
        'xp_2_session': xp_2_session,
        'xp_3_session': xp_3_session,
        'xp_4_session': xp_4_session,
        'xp_5_session': xp_5_session,
        'xp_6_session': xp_6_session,
        'xp_1_desc': xp_1_desc,
        'xp_2_desc': xp_2_desc,
        'xp_3_desc': xp_3_desc,
        'xp_4_desc': xp_4_desc,
        'xp_5_desc': xp_5_desc,
        'xp_6_desc': xp_6_desc,
        'user_id': user_id}]
        }

        result = (str(context))
    response = HttpResponse(result)
    return (response)
