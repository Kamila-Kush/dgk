from django.shortcuts import render, HttpResponse

def homepage(request):
    if request.method == "POST":
        return HttpResponse("Метод не разрешён, только GET", status=405)
    return render(request=request, template_name="index.html")