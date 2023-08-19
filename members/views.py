from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.

def home(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def members(request):
    my_members = Members.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "my_members": my_members
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    member_detail = Members.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "member_detail": member_detail
    }

    return HttpResponse(template.render(context, request))