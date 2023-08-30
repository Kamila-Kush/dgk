from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import *

def homepage(request):
    if request.method == "POST":
        return HttpResponse("Метод не разрешён, только GET", status=405)
    return render(request=request, template_name="index.html")

def about_us(request):
    return render(request=request, template_name="about_us.html")

def structure_of_company(request):
    return render(request=request, template_name="structure_of_company.html")

def corporative_culture(request):
    return render(request=request, template_name="culture.html")

class ManagementList(ListView):
    template_name = "management.html"
    model = Management

