# from django.shortcuts import render, HttpResponse

# # Create your views here.
# def home(request):
#     return HttpResponse("Hello World!, You are at the home page of basicapp.")

from django.shortcuts import render
from .models import todoitem
def home(request):
    return render(request, "home.html")

def todo(request):
    # items = todo.objects.all().order_by("created")
    items = todoitem.objects.all()
    return render(request, "todo.html", {"todos": items})