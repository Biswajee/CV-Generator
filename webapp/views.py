from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import User, UserData

context = {}


def index(request):
    return render(request, "webpages/index.html")


def signup(request):
    return render(request, "webpages/signup.html")


def signupinfo(request):
    try:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            phone = request.POST["phone"]
            name = request.POST["name"]

            registration = User(
                email=email,
                password=password,
                phone=phone,
                name=name,
            )
            registration.save()

            user_signup_info = {"email": email, "user_id": registration.id}
            return render(request, "webpages/signupdata.html", user_signup_info)
        else:
            return render(
                request,
                "webpages/signup.html",
                {"error": "Some error occoured ! Check back later."},
            )
    except:
        return render(
            request, "webpages/signup.html", {"error": "Email ID is already registered !"}
        )


def signin(request):
    if request.user.is_authenticated:
        return redirect("webpages/fillform.html")
    else:
        return render(request, "webpages/signin.html")


def verify(request):
    try:
        if request.method == "POST":
            email = request.POST.get("email", "empty")
            password = request.POST.get("password", "empty")
            if User.objects.get(Q(email=email) & Q(password=password)):
                return HttpResponse(
                    (loader.get_template("webpages/fillform.html")).render(
                        {
                            "name": (
                                User.objects.get(Q(email=email) & Q(password=password))
                            ).name
                        },
                        request,
                    )
                )
            else:
                return render(request, "webpages/signin.html", {"data": "Login Unsuccessful"})
        else:
            return render(request, "webpages/signin.html", {"data": "Login Unsuccessful"})
    except:
        return render(request, "webpages/signin.html", {"data": "Technical Error occured !"})


def formfill(request):
    return render(request, "webpages/fillform.html")


def profile(request):
    return render(request, "webpages/signin.html")


def read_docs(request):
    return render(request, "webpages/read_docs.html")


def form_submit(request):
    try:
        if request.method == "POST":
            user_id = request.session["uid"]

            # Introduction vars
            name = request.POST["nm"]
            position = request.POST["position"]
            univ = request.POST["univ"]
            session = request.POST["session"]
            email = request.POST["email"]
            ph = request.POST["ph"]
            cph = request.POST["cph"]
            cemail = request.POST["cemail"]
            desc = request.POST["desc"]

            # Academic Qualification

            cgpa = request.POST["cgpa"]

            # Skill variables

            skill_1 = request.POST["skill_1"]
            skill_2 = request.POST["skill_2"]
            skill_3 = request.POST["skill_3"]
            skill_4 = request.POST["skill_4"]
            skill_5 = request.POST["skill_5"]
            skill_6 = request.POST["skill_6"]

            # Work Experience

            xp_1_title = request.POST["xp_1_title"]
            xp_1_session = request.POST["xp_1_session"]
            xp_1_desc = request.POST["xp_1_desc"]

            xp_2_title = request.POST["xp_2_title"]
            xp_2_session = request.POST["xp_2_session"]
            xp_2_desc = request.POST["xp_2_desc"]

            xp_3_title = request.POST["xp_3_title"]
            xp_3_session = request.POST["xp_3_session"]
            xp_3_desc = request.POST["xp_3_desc"]

            xp_4_title = request.POST["xp_4_title"]
            xp_4_session = request.POST["xp_4_session"]
            xp_4_desc = request.POST["xp_4_desc"]

            xp_5_title = request.POST["xp_5_title"]
            xp_5_session = request.POST["xp_5_session"]
            xp_5_desc = request.POST["xp_5_desc"]

            xp_6_title = request.POST["xp_6_title"]
            xp_6_session = request.POST["xp_6_session"]
            xp_6_desc = request.POST["xp_6_desc"]

            user_data = UserData(
                name=name,
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
                usr_id_id=user_id,
            )
            user_data.save()

            context = {
                "name": name,
                "position": position,
                "univ": univ,
                "session": session,
                "email": email,
                "ph": ph,
                "cph": cph,
                "cemail": cemail,
                "desc": desc,
                "cgpa": cgpa,
                "skill_1": skill_1,
                "skill_2": skill_2,
                "skill_3": skill_3,
                "skill_4": skill_4,
                "skill_5": skill_5,
                "skill_6": skill_6,
                "xp_1_title": xp_1_title,
                "xp_2_title": xp_2_title,
                "xp_3_title": xp_3_title,
                "xp_4_title": xp_4_title,
                "xp_5_title": xp_5_title,
                "xp_6_title": xp_6_title,
                "xp_1_session": xp_1_session,
                "xp_2_session": xp_2_session,
                "xp_3_session": xp_3_session,
                "xp_4_session": xp_4_session,
                "xp_5_session": xp_5_session,
                "xp_6_session": xp_6_session,
                "xp_1_desc": xp_1_desc,
                "xp_2_desc": xp_2_desc,
                "xp_3_desc": xp_3_desc,
                "xp_4_desc": xp_4_desc,
                "xp_5_desc": xp_5_desc,
                "xp_6_desc": xp_6_desc,
                "user_id": user_id,
            }

            return render(request, "webpages/good_resume.html", context)
        else:
            return render(
                request, "webpages/fillform.html", {"notice": "Form accepts POST Requests only"}
            )
    except:
        return render(
            request, "webpages/fillform.html", {"notice": "Please fill all fields correctly"}
        )


def logout(request):
    try:
        request.session.modified = True
        return render(request, "webpages/logout.html")
    except:
        return render(
            request,
            "webpages/logout.html",
            {"message": "You are already logged out", "style": "none"},
        )
