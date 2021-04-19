from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.

def root(request):
    return redirect("blogs")

def index(request):
    return HttpResponse("<h1>placeholder to later display a list of all blogs</h1>")

def new(request):
	return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
	return HttpResponseRedirect("/")

def show(request, number):
	return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
	return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
	return HttpResponseRedirect("/")

def json(request):
	return JsonResponse({"response": "JSON response from redirected_method", "status": True})