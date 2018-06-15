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
    name = request.form['nm']
    position = request.form['position']
    univ = request.form['univ']
    session = request.form['session']
    email = request.form['email']
    ph = request.form['ph']
    cph = request.form['cph']
    cemail = request.form['cemail']
    fax = request.form['fax']
    desc = request.form['desc']

    # Academic Qualification

    cgpa = request.form['cgpa']

    # Skill variables

    skill_1 = request.form['skill_1']
    skill_2 = request.form['skill_2']
    skill_3 = request.form['skill_3']
    skill_4 = request.form['skill_4']
    skill_5 = request.form['skill_5']
    skill_6 = request.form['skill_6']


    # Work Experience

    xp_1_title = request.form['xp_1_title']
    xp_1_session = request.form['xp_1_session']
    xp_1_desc = request.form['xp_1_desc']

    xp_2_title = request.form['xp_2_title']
    xp_2_session = request.form['xp_2_session']
    xp_2_desc = request.form['xp_2_desc']

    xp_3_title = request.form['xp_3_title']
    xp_3_session = request.form['xp_3_session']
    xp_3_desc = request.form['xp_3_desc']

    xp_4_title = request.form['xp_4_title']
    xp_4_session = request.form['xp_4_session']
    xp_4_desc = request.form['xp_4_desc']

    xp_5_title = request.form['xp_5_title']
    xp_5_session = request.form['xp_5_session']
    xp_5_desc = request.form['xp_5_desc']

    xp_6_title = request.form['xp_6_title']
    xp_6_session = request.form['xp_6_session']
    xp_6_desc = request.form['xp_6_desc']

    context = {
                'name':name,
                'position':position,
                'univ': univ,
                'session': session,
                'email': email,
                'ph': ph,
                'cph': cph,
                'cemail': cemail,
                'fax': fax,
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


    return render(request, 'webpages/resume.html', context)
