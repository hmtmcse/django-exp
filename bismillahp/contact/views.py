from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Contact Bismillah View")


def form(request):
    return render(request, 'contact/form.html')


def layout_extends(request):
    return render(request, 'contact/layout-extends.html')
