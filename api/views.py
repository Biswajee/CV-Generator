from django.shortcuts import render
from webapp.models import resume_data, generateId, reg_info
from django.http import HttpResponse
# Create your views here.


def json_endpoint(request):
    db_data = resume_data.objects.all()
    print(resume_data.objects.all())
    response = HttpResponse(db_data)
    return response
