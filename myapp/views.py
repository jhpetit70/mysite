from django.http import HttpResponse, JsonResponse
from .models import Project


# Create your views here.
def index(request):
    return HttpResponse("Index page")


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    return HttpResponse("About")


def projects(resquest):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def task(resquest):
    return HttpResponse("task")
