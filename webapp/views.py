from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from flask import jsonify
from .models import resume_data, generateId, reg_info
from datetime import datetime
from django.db.models import Q

# Create your views here.

context = {}

def index(request):
    return render(request, 'webpages/index.html')


def signup(request):
    user_id = generateId()
    request.session["uid"] = user_id
    return render(request, 'webpages/signup.html')

def signupinfo(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            user_id = request.session["uid"]
            password = request.POST['password']
            phone = request.POST['phone']
            name = request.POST['name']

            user_reg_data = reg_info(usr_id=user_id,
                                 email=email,
                                 password=password,
                                 phone=phone,
                                 name=name,
                                 date=datetime.now())
            user_reg_data.save()


            user_signup_info = {'user_id': user_id, 'email': email }
            return render(request, 'webpages/signupdata.html', user_signup_info)
        else:
            return render(request, 'webpages/signup.html', {'error': "Some error occoured ! Check back later."})
    except:
            return render(request, 'webpages/signup.html', {'error': "Email ID is already registered !"})


def signin(request):
    if request.user.is_authenticated:
        return redirect('webpages/fillform.html')
    else:
        return render(request, 'webpages/signin.html')


def verify(request):
    try :
        if request.method == 'POST':
            email = request.POST.get('email','empty')
            password=request.POST.get('password','empty')
            if reg_info.objects.get(Q(email = email ) & Q(password=password)):
                return HttpResponse((loader.get_template('webpages/fillform.html')).render({'name':(reg_info.objects.get(Q(email = email) & Q(password = password))).name}, request))
            else:
                return render(request, 'webpages/signin.html',{'data': "Login Unsuccessful"})
        else:
            return render(request, 'webpages/signin.html',{'data': "Login Unsuccessful"})
    except :
        return render(request, 'webpages/signin.html',{'data': "Technical Error occured !"})


def formfill(request):
    return render(request, 'webpages/fillform.html')

def profile(request):
    return render(request, 'webpages/signin.html')

def read_docs(request):
    return render(request, 'webpages/read_docs.html')

def form_submit(request):

    try:
        if request.method == 'POST':

            user_id = request.session["uid"]

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

            user_data = resume_data(name=name,
                                position=position,
                                univ=univ,
                                session=session,
                                email=email,
                                ph=ph,
                                cph=cph,
                                cemail=cemail,
                                desc=desc,
                                cgpa=cgpa,
                                skill_1=skill_1,
                                skill_2=skill_2,
                                skill_3=skill_3,
                                skill_4=skill_4,
                                skill_5=skill_5,
                                skill_6=skill_6,
                                xp_1_title=xp_1_title,
                                xp_2_title=xp_2_title,
                                xp_3_title=xp_3_title,
                                xp_4_title=xp_4_title,
                                xp_5_title=xp_5_title,
                                xp_6_title=xp_6_title,
                                xp_1_session=xp_1_session,
                                xp_2_session=xp_2_session,
                                xp_3_session=xp_3_session,
                                xp_4_session=xp_4_session,
                                xp_5_session=xp_5_session,
                                xp_6_session=xp_6_session,
                                xp_1_desc=xp_1_desc,
                                xp_2_desc=xp_2_desc,
                                xp_3_desc=xp_3_desc,
                                xp_4_desc=xp_4_desc,
                                xp_5_desc=xp_5_desc,
                                xp_6_desc=xp_6_desc,
                                usr_id_id=user_id
                                )
            user_data.save()


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
                'user_id': user_id
                    }

            return render(request, 'webpages/good_resume.html', context)
        else:
            return render(request, 'webpages/fillform.html', {'notice': "Form accepts POST Requests only"})
    except:
        return render(request, 'webpages/fillform.html', {'notice': "Please fill all fields correctly"})
