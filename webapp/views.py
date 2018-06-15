from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse


import os
import jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates/webpages')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


# Create your views here.

context = {}

def index(request):
    return render(request, 'webpages/index.html')


def signup(request):
    return render(request, 'webpages/signup.html')


def signin(request):
    return render(request, 'webpages/signin.html')


def formfill(request):
    return render(request, 'webpages/fillform.html')

def profile(request):
    return render(request, 'webpages/signin.html')

def read_docs(request):
    return render(request, 'webpages/read_docs.html')

def form_submit(request):
    template = jinja_env.get_template('resume.html')

    # Introduction vars
    name = request.POST['nm']
    position = request.POST['position']
    univ = request.POST['univ']
    session = request.POST['session']
    email = request.POST['email']
    ph = request.POST['ph']
    cph = request.POST['cph']
    cemail = request.POST['cemail']
    desc = request.POST['desc']

    # Academic Qualification

    cgpa = request.POST['cgpa']

    # Skill variables

    skill_1 = request.POST['skill_1']
    skill_2 = request.POST['skill_2']
    skill_3 = request.POST['skill_3']
    skill_4 = request.POST['skill_4']
    skill_5 = request.POST['skill_5']
    skill_6 = request.POST['skill_6']


    # Work Experience

    xp_1_title = request.POST['xp_1_title']
    xp_1_session = request.POST['xp_1_session']
    xp_1_desc = request.POST['xp_1_desc']

    xp_2_title = request.POST['xp_2_title']
    xp_2_session = request.POST['xp_2_session']
    xp_2_desc = request.POST['xp_2_desc']

    xp_3_title = request.POST['xp_3_title']
    xp_3_session = request.POST['xp_3_session']
    xp_3_desc = request.POST['xp_3_desc']

    xp_4_title = request.POST['xp_4_title']
    xp_4_session = request.POST['xp_4_session']
    xp_4_desc = request.POST['xp_4_desc']

    xp_5_title = request.POST['xp_5_title']
    xp_5_session = request.POST['xp_5_session']
    xp_5_desc = request.POST['xp_5_desc']

    xp_6_title = request.POST['xp_6_title']
    xp_6_session = request.POST['xp_6_session']
    xp_6_desc = request.POST['xp_6_desc']

    context = {
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
                }


    return render(request, 'webpages/good_resume.html', context)
